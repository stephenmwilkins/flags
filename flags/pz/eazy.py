


import io
import sys
import os
import tempfile
import numpy as np
import h5py
from astropy.io import ascii



class Eazy():

    def __init__(self, id, fc, EAZY_working_dir = 'EAZY', path_to_EAZY = os.getenv('EAZY'), create_POFZ_FILE = False):

        self.ID = id
        self.fc = fc

        # --- create EAZY working directory if it doesn't already exist

        self.EAZY_working_dir = EAZY_working_dir
        self.path_to_EAZY = path_to_EAZY

        self.create_POFZ_FILE = create_POFZ_FILE

        if not os.path.exists(EAZY_working_dir):
            os.mkdir(EAZY_working_dir)
            os.mkdir(f'{EAZY_working_dir}/inputs')
            os.mkdir(f'{EAZY_working_dir}/outputs')

            # --- create symbolic link to templates
        if not os.path.exists(f'templates'):
            os.symlink(f'{path_to_EAZY}/templates', f'templates')

        self.create_param()
        self.create_filter_RES()


    def create_filter_RES(self):

        """ Take a flare filter object and create a EAZY RES file """

        self.filters = self.fc.filters

        # --- create filter RES file
        create_EAZY_filter_res(self.fc, filter_res_file = f'{self.EAZY_working_dir}/inputs/{self.ID}.RES')



    def run(self):

        """ Saves the input file and runs EAZY """

        # --- write the parameter file to the inputs directory
        write_param_file(f'{self.EAZY_working_dir}/inputs/{self.ID}.param', self.params)



        # --- run EAZY

        eazy_cmd = f'{self.path_to_EAZY}/src/eazy -p {self.EAZY_working_dir}/inputs/{self.ID}.param'
        print(eazy_cmd)

        os.system(eazy_cmd)

        # --- read EAZY output
        # return get_EAZY_output_as_HDF5(f'{self.EAZY_working_dir}/outputs/{self.ID}', read_POFZ_FILE = self.create_POFZ_FILE, output_file = output_file)


    def create_param(self):

        """ Create a default parameter dictionary """

        self.params = default_params(self.EAZY_working_dir)
        self.params['CATALOG_FILE'] = f'{self.EAZY_working_dir}/inputs/{self.ID}.cat'
        self.params['MAIN_OUTPUT_FILE'] = f'{self.ID}'
        self.params['FILTERS_RES'] = f'{self.EAZY_working_dir}/inputs/{self.ID}.RES'

        if self.create_POFZ_FILE: self.params['POFZ_FILE'] = 'y'


    def create_input_catalogue_from_HDF5(self, hf, path = lambda f: f'obs/{f}'):

        N = len(hf[f'{path(self.filters[-1])}/flux'][()])

        table = {'#id': np.arange(N)}

        for i, f in enumerate(self.filters):
            table['F'+str(i+1)] = hf[f'{path(f)}/flux'][()]
            table['E'+str(i+1)] = hf[f'{path(f)}/flux_err'][()]

        flatten = lambda l: [item for sublist in l for item in sublist]
        names = ['#id'] + flatten([['F'+str(i+1), 'E'+str(i+1)] for i in range(len(self.filters))])

        ascii.write(table, f'{self.EAZY_working_dir}/inputs/{self.ID}.cat', names=names, overwrite=True)







def create_EAZY_filter_res(fc, filter_res_file = 'FILTER.RES'):

    o = []

    for f in fc.filters:

        o.append('{n} {f}\n'.format(n=len(fc.filter[f].lam), f=f)) # filter header

        for i,l in enumerate(fc.filter[f].lam):
            o.append('{i:>5}   {l}   {t}\n'.format(i=i+1, l=l,t=fc.filter[f].t[i]))

    open(filter_res_file,'w').writelines(o)



def read_zout(filename):

    zout_table = ascii.read(f'{filename}.zout')

    return {c: zout_table[c].data for c in list(zout_table.columns)}


def read_temp_sed(filename, id):

    temp_sed = ascii.read(f'{filename}_{id}.temp_sed')

    h = temp_sed.meta['comments'][0]
    h = h.replace(': ', ':')
    h = h.replace('z= ', 'z:')
    meta = {}
    for h_ in h.split(' '):
        k, v = h_.split(':')
        try:
            meta[k] = np.float(v)
        except:
            pass

    template_norm = np.expand_dims(np.array([meta[str(i+1)] for i in range(len(meta.keys())-1)]),1)

    z = meta['z']

    lam = temp_sed['lambda'].data
    fnu = temp_sed['tempflux'].data

    return z, template_norm, lam, fnu


def read_template_norm(filename, id):

    with open(f'{filename}_{id}.temp_sed','r') as f:
        h = f.readlines()[1][2:]

    h = h.replace(': ', ':')
    h = h.replace('z= ', 'z:')
    h = h.replace('z=', 'z:')
    meta = {}
    for h_ in h.split(' '):
        k, v = h_.split(':')
        try:
            meta[k] = np.float(v)
        except:
            pass

    template_norm = [meta[str(i+1)] for i in range(len(meta.keys())-1)]

    return template_norm


def read_template_norms(filename, ids):

    template_norm = read_template_norm(filename, ids[0])

    template_norms = np.zeros((len(ids), len(template_norm)))

    for i, id in enumerate(ids):

        template_norms[i] = read_template_norm(filename, id)

    return template_norms



def read_pz(filename, id):

    pz_ = ascii.read(f'{filename}_{id}.pz')
    z = pz_['col1'].data
    dz = z[1]-z[0]
    chi2 = pz_['col2'].data
    pz = np.exp(-chi2)
    pz /= np.sum(pz)*dz # needs normalising

    return z, chi2, pz


def read_pzs(filename, ids):

    z, _, _ = read_pz(filename, ids[0]) # -- read first pz file to get length

    chi2 = np.zeros((len(ids), len(z)))
    pz = np.zeros((len(ids), len(z)))

    for i, id in enumerate(ids):

        z_, chi2_, pz_ = read_pz(filename, id)

        chi2[i] = chi2_
        pz[i] = pz_

    return z, chi2, pz









# def get_EAZY_output_as_HDF5(filename, read_POFZ_FILE = False, output_file = False, group_name = 'EAZY'):
#
#     if output_file:
#         hf = h5py.File(output_file, 'a')
#     else:
#         # --- create a temporary file
#         bio = io.BytesIO()
#         hf = h5py.File(bio)
#
#     zout, POFZ = read_EAZY_output(filename, read_POFZ_FILE = read_POFZ_FILE)
#
#     g = hf.create_group(group_name)
#
#     for k, v in zout.items():
#         g.create_dataset(k, data = v)
#
#     return hf


def append_EAZY_output_to_HDF5(filename, hf, read_pz = False, read_template_norm = False, group_name = 'pz/eazy'):

    zout = read_zout(filename)

    g = hf.create_group(group_name)

    for k, v in zout.items():
        g.create_dataset(k, data = v)

    ids = zout['id']

    if read_pz:
        z, chi2, pz = read_pzs(filename, ids)
        g.create_dataset('p_of_z/z', data = z)
        g.create_dataset('p_of_z/chi2', data = chi2)
        g.create_dataset('p_of_z/pz', data = pz)

    if read_template_norm:
        template_norms = read_template_norms(filename, ids)
        g.create_dataset('template_norms', data = template_norms)


class template:
    pass


def get_templates(template_set, path_to_EAZY = os.getenv('EAZY')):

    params = ascii.read(f'{path_to_EAZY}/templates/{template_set}', names = ['Template number', 'Template file name', 'Lambda_conv', 'Age', 'Template error amplitude'])
    print(params)

    templates = {}

    for template_number, template_file_name, template_age in zip(params['Template number'].data, params['Template file name'].data, params['Age'].data):

        lam, flam = np.loadtxt(f'{path_to_EAZY}/{template_file_name}', unpack = True)

        t = template()
        t.number = template_number
        t.file_name = template_file_name
        t.age = template_age
        t.lam = lam
        t.log10lam = np.log10(lam)
        t.flam = flam
        t.fnu = flam * t.lam**2*1E-10*1E11/3E8 # normalisation doesn't matter

        templates[template_number] = t

    return templates


def get_template_grid(templates):

    fnu = []
    for t in templates.values():
        lam = t.lam
        fnu.append(t.fnu)

    return lam, np.array(fnu)










def default_params(EAZY_working_dir):

    #### EAZY Default parameters

    params = {}

    ## Filters
    params['FILTERS_RES'] = 'FILTER.RES.latest'  # Filter transmission data
    params['FILTER_FORMAT'] = 1                  # Format of FILTERS_RES file -- 0: energy-  1: photon-counting detector
    params['SMOOTH_FILTERS'] = 'n'                  # Smooth filter curves with Gaussian
    params['SMOOTH_SIGMA'] = 100.               # Gaussian sigma (in Angstroms) to smooth filters

    ## Templates
    params['TEMPLATES_FILE'] = f'templates/eazy_v1.2_dusty.spectra.param' # Template definition file
    params['TEMPLATE_COMBOS'] = 'a'                  # Template combination options:
                                            #         1 : one template at a time
                                            #         2 : two templates, read allowed combinations from TEMPLATES_FILE
                                            #        -2 : two templates, all permutations
                                            # a <or> 99 : all templates simultaneously
    params['NMF_TOLERANCE']=1.e-4              # Tolerance for non-negative combinations (TEMPLATE_COMBOS=a)
    params['WAVELENGTH_FILE']=f'templates/EAZY_v1.1_lines/lambda_v1.1.def' # Wavelength grid definition file
    params['TEMP_ERR_FILE']=f'templates/TEMPLATE_ERROR.eazy_v1.0' # Template error definition file
    params['TEMP_ERR_A2']=0.50               # Template error amplitude
    params['SYS_ERR']=0.00               # Systematic flux error (% of flux)
    params['APPLY_IGM']='y'                  # Apply Madau 1995 IGM absorption
    params['LAF_FILE']=f'templates/LAFcoeff.txt' # File containing the Lyman alpha forest data from Inoue
    params['DLA_FILE']=f'templates/DLAcoeff.txt' # File containing the damped Lyman absorber data from Inoue
    params['SCALE_2175_BUMP']=0.00               # Scaling of 2175A bump.  Values 0.13 (0.27) absorb ~10 (20) % at peak.

    params['DUMP_TEMPLATE_CACHE']='n'                  # Write binary template cache
    params['USE_TEMPLATE_CACHE']='n'                  # Load in template cache
    params['CACHE_FILE']='photz.tempfilt'     # Template cache file (in OUTPUT_DIRECTORY)

    ## Input Files
    params['CATALOG_FILE']='hdfn_fs99_eazy.cat' # Catalog data file
    params['MAGNITUDES']='n'                  # Catalog photometry in magnitudes rather than f_nu fluxes
    params['NOT_OBS_THRESHOLD']=-90                # Ignore flux point if <NOT_OBS_THRESH
    params['N_MIN_COLORS']=3                  # Require N_MIN_COLORS to fit

    ## Output Files
    params['OUTPUT_DIRECTORY']=f'{EAZY_working_dir}/outputs'          # Directory to put output files in
    params['MAIN_OUTPUT_FILE']='photz'              # Main output file, .zout
    params['PRINT_ERRORS']='y'                  # Print 68, 95 and 99% confidence intervals
    params['CHI2_SCALE']=1.0                # Scale ML Chi-squared values to improve confidence intervals
    params['VERBOSE_LOG']='y'                  # Dump information from the run into [MAIN_OUTPUT_FILE].param
    params['OBS_SED_FILE']='n'                  # Write out observed SED/object, .obs_sed
    params['TEMP_SED_FILE']='n'                   # Write out best template fit/object, .temp_sed
    params['POFZ_FILE']='n'                   # Write out Pofz/object, .pz
    params['BINARY_OUTPUT']='n'                 # Save OBS_SED, TEMP_SED, PZ in binary format to read with e.g IDL

    ## Redshift / Mag prior
    params['APPLY_PRIOR']='n'                  # Apply apparent magnitude prior
    params['PRIOR_FILE']=f'templates/prior_K_extend.dat' # File containing prior grid
    params['PRIOR_FILTER']=28                 # Filter from FILTER_RES corresponding to the columns in PRIOR_FILE
    params['PRIOR_ABZP']=25.0               # AB zeropoint of fluxes in catalog.  Needed for calculating apparent mags!

    ## Redshift Grid
    params['FIX_ZSPEC']='n'                  # Fix redshift to catalog zspec
    params['Z_MIN']=0.01               # Minimum redshift
    params['Z_MAX']=20.00               # Maximum redshift
    params['Z_STEP']=0.01               # Redshift step size
    params['Z_STEP_TYPE']=0                  #  0 = ZSTEP, 1 = Z_STEP*(1+z)

    ## Zeropoint Offsets
    params['GET_ZP_OFFSETS']='n'                  # Look for zphot.zeropoint file and compute zeropoint offsets
    params['ZP_OFFSET_TOL']=1.E-4              # Tolerance for iterative fit for zeropoint offsets [not implemented]

    ## Rest-frame colors
    params['REST_FILTERS']='---'                # Comma-separated list of rest frame filters to compute
    params['RF_PADDING']=1000.              # Padding (Ang) for choosing observed filters around specified rest-frame pair.
    params['RF_ERRORS']='n'                  # Compute RF color errors from p(z)
    params['Z_COLUMN']='z_peak'             # Redshift to use for rest-frame color calculation (z_a, z_p, z_m1, z_m2, z_peak)
    params['USE_ZSPEC_FOR_REST']='y'                  # Use z_spec when available for rest-frame colors
    params['READ_ZBIN']='n'                  # Get redshifts from OUTPUT_DIRECTORY/MAIN_OUTPUT_FILE.zbin rather than fitting them.

    ## Cosmology
    params['H0']=70.0               # Hubble constant (km/s/Mpc)
    params['OMEGA_M']=0.3                # Omega_matter
    params['OMEGA_L']=0.7                # Omega_lambda

    return params


def write_param_file(filename, params):

    lines = [f'{k}\t {v}\n' for k,v in params.items()]

    open(filename,'w').writelines(lines)
