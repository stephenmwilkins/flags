

import io
import sys
import os
import tempfile
import numpy as np
import h5py
from astropy.io import ascii


class Eazy():

    def __init__(self, id, fc, params = None, eazy_working_dir='eazy', path_to_eazy=os.getenv('EAZY'), create_POFZ_FILE=False):

        self.id = id
        self.fc = fc

        print(self.id)

        # --- create EAZY working directory if it doesn't already exist

        self.eazy_working_dir = eazy_working_dir
        self.path_to_eaxy = path_to_eazy

        self.create_POFZ_FILE = create_POFZ_FILE

        if not os.path.exists(eazy_working_dir):
            os.mkdir(eazy_working_dir)
            os.mkdir(f'{eazy_working_dir}/inputs')
            os.mkdir(f'{eazy_working_dir}/outputs')
            print('created EAZY working directory')

            # --- create symbolic link to templates
        if not os.path.exists(f'templates'):
            try:
                os.symlink(f'{path_to_eazy}/templates', f'templates', target_is_directory=True)
                print('Created link to EAZY templates')
            except:
                print('Failed to create link to EAZY templates')


        # if no parameter dictionary supplied, use the default. NOT yet implemented
        if not params:
            print('NO PARAMETER DICTIONARY PROVIDED, DEFAULTS NOT YET IMPLEMENTED')
        else:
            self.params = params


        # change some defaults
        self.params['CATALOG_FILE'] = f'{self.eazy_working_dir}/inputs/{self.id}.cat'
        self.params['MAIN_OUTPUT_FILE'] = f'{self.id}'
        self.params['FILTERS_RES'] = f'{self.eazy_working_dir}/inputs/{self.id}.RES'

        if self.create_POFZ_FILE:
            self.params['POFZ_FILE'] = 'y'


        for k, v in self.params.items():
            print(f'{k} : {v}')
    
        # create filter resource file
        self.create_filter_RES()

    def create_filter_RES(self):
        """ Take a flare filter object and create a EAZY RES file """

        self.filters = self.fc.filter_codes

        # --- create filter RES file
        create_EAZY_filter_res(
            self.fc, filter_res_file=f'{self.eazy_working_dir}/inputs/{self.id}.RES')

    def run(self):
        """ Saves the input file and runs EAZY """

        # --- write the parameter file to the inputs directory
        write_param_file(f'{self.eazy_working_dir}/inputs/{self.id}.param', self.params)

        # --- run EAZY

        eazy_cmd = f'{self.path_to_eaxy}/src/eazy -p {self.eazy_working_dir}/inputs/{self.id}.param'
        print(eazy_cmd)

        os.system(eazy_cmd)

        # --- read EAZY output
        # return get_EAZY_output_as_HDF5(f'{self.eazy_working_dir}/outputs/{self.id}', read_POFZ_FILE = self.create_POFZ_FILE, output_file = output_file)

   
        

    def create_input_catalogue_from_HDF5(self, hf, flux_path=lambda f: f'obs/{f}/flux', flux_err_path = lambda f: f'obs/{f}/flux_err'):

        """
        Create an EAZY input from a HDF5 file by giving it a function that points to the flux and error as a function of the filter.
        """

        N = len(hf[f'{flux_path(self.filters[-1])}'][()])

        table = {'#id': np.arange(N)}

        for i, f in enumerate(self.filters):
            table['F'+str(i+1)] = hf[f'{flux_path(f)}'][()]
            table['E'+str(i+1)] = hf[f'{flux_err_path(f)}'][()]

        def flatten(l): return [item for sublist in l for item in sublist]
        names = ['#id'] + flatten([['F'+str(i+1), 'E'+str(i+1)] for i in range(len(self.filters))])

        ascii.write(table, f'{self.eazy_working_dir}/inputs/{self.id}.cat',
                    names=names, overwrite=True)


    def create_input_catalogue_from_dict(self, flux_dict, err_dict):

        """
        Create an EAZY input file from a pair of dictionaries describing the flux and error  
        """

        filters = list(flux_dict.keys())

        N = len(flux_dict[filters[0]])

        table = {'#id': np.arange(N)}

        for i, f in enumerate(filters):
            table['F'+str(i+1)] = flux_dict[f]
            table['E'+str(i+1)] = err_dict[f]

        def flatten(l): return [item for sublist in l for item in sublist]
        names = ['#id'] + flatten([['F'+str(i+1), 'E'+str(i+1)] for i in range(len(self.filters))])

        ascii.write(table, f'{self.eazy_working_dir}/inputs/{self.id}.cat',
                    names=names, overwrite=True)



def create_EAZY_filter_res(fc, filter_res_file='FILTER.RES'):

    o = []

    for f in fc:
        o.append('{n} {f}\n'.format(n=len(f.original_lam), f=f.filter_code))  # filter header

        for i, l in enumerate(f.original_lam):
            o.append('{i:>5}   {l}   {t}\n'.format(i=i+1, l=l, t=f.original_t[i]))

    open(filter_res_file, 'w').writelines(o)


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

    template_norm = np.expand_dims(np.array([meta[str(i+1)] for i in range(len(meta.keys())-1)]), 1)

    z = meta['z']

    lam = temp_sed['lambda'].data
    fnu = temp_sed['tempflux'].data

    return z, template_norm, lam, fnu


def read_template_norm(filename, id):

    with open(f'{filename}_{id}.temp_sed', 'r') as f:
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
    pz /= np.sum(pz)*dz  # needs normalising

    return z, chi2, pz, dz


def read_pzs(filename, ids):

    z, _, _, dz = read_pz(filename, ids[0])  # -- read first pz file to get length

    chi2 = np.zeros((len(ids), len(z)))
    pz = np.zeros((len(ids), len(z)))

    for i, id in enumerate(ids):

        z_, chi2_, pz_, dz = read_pz(filename, id)

        chi2[i] = chi2_
        pz[i] = pz_

    return z, chi2, pz, dz


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


def append_EAZY_output_to_HDF5(filename, hf, read_pz=False, read_template_norm=False, get_integrals=False, group_name='pz/eazy'):

    zout = read_zout(filename)

    g = hf.create_group(group_name)

    for k, v in zout.items():
        g.create_dataset(k, data=v)

    ids = zout['id']

    if read_pz:
        z, chi2, pz, dz = read_pzs(filename, ids)
        g.create_dataset('p_of_z/z', data=z)
        g.create_dataset('p_of_z/chi2', data=chi2)
        g.create_dataset('p_of_z/pz', data=pz)

    if get_integrals:
        if not read_pz:
            z, chi2_, pz_, dz = read_pzs(filename, ids)

        # for i, pz in enumerate(pz_):
        #     print('-'*100)
        #     print(i)
        #     print(z, pz)
        #     for redshift in np.arange(0, 15, 1):
        #         print(redshift, dz*np.sum(pz[z >= redshift]))

        for redshift in np.arange(0, 15, 1):

            int_zgt = np.empty(len(pz_))

            for i, pz in enumerate(pz_):
                int_zgt[i] = dz*np.sum(pz[z >= redshift])

            g.create_dataset(f'INT_ZGT{redshift}', data=int_zgt)

    if read_template_norm:
        template_norms = read_template_norms(filename, ids)
        g.create_dataset('template_norms', data=template_norms)


class template:
    pass


def get_templates(template_set, path_to_eaxy=os.getenv('EAZY')):

    params = ascii.read(f'{path_to_eaxy}/templates/{template_set}', names=[
                        'Template number', 'Template file name', 'Lambda_conv', 'Age', 'Template error amplitude'])
    print(params)

    templates = {}

    for template_number, template_file_name, template_age in zip(params['Template number'].data, params['Template file name'].data, params['Age'].data):

        lam, flam = np.loadtxt(f'{path_to_eaxy}/{template_file_name}', unpack=True)

        t = template()
        t.number = template_number
        t.file_name = template_file_name
        t.age = template_age
        t.lam = lam
        t.log10lam = np.log10(lam)
        t.flam = flam
        t.fnu = flam * t.lam**2*1E-10*1E11/3E8  # normalisation doesn't matter

        templates[template_number] = t

    return templates


def get_template_grid(templates):

    fnu = []
    for t in templates.values():
        lam = t.lam
        fnu.append(t.fnu)

    return lam, np.array(fnu)


def write_param_file(filename, params):

    lines = [f'{k}\t {v}\n' for k, v in params.items()]

    open(filename, 'w').writelines(lines)
