
import numpy as np
from .utils import Survey, combine_surveys, combine_fields

survey = {}


# --- simple scenarios
# default_ratio = {'JWST/NIRCam.F070W': 8.13, 'JWST/NIRCam.F090W': 6.67, 'JWST/NIRCam.F115W': 6.08, 'JWST/NIRCam.F150W': 4.83, 'JWST/NIRCam.F200W': 3.98, 'JWST/NIRCam.F277W': 4.70, 'JWST/NIRCam.F356W':6.58, 'JWST/NIRCam.F356W': 3.91, 'JWST/NIRCam.F410M': 7.56, 'JWST/NIRCam.F444W': 5.95} # 'Hubble.ACS.f814w': 6.08,
default_ratio = {'JWST/NIRCam.F090W': 6.67, 'JWST/NIRCam.F115W': 6.08, 'JWST/NIRCam.F150W': 4.83, 'JWST/NIRCam.F200W': 3.98, 'JWST/NIRCam.F277W': 4.70, 'JWST/NIRCam.F356W':6.58, 'JWST/NIRCam.F356W': 3.91, 'JWST/NIRCam.F410M': 7.56, 'JWST/NIRCam.F444W': 5.95} # 'Hubble.ACS.f814w': 6.08,
survey['fiducial'] = Survey('fiducial', depth_reference_filter = 'JWST/NIRCam.F150W')
for ref_depth_mag, tier in zip([27., 28., 29., 30., 31.], ['ushallow', 'shallow', 'medium', 'deep', 'udeep']):
    depths_mag = {filter: ref_depth_mag - 2.5*np.log10(v/default_ratio['JWST/NIRCam.F200W']) for filter, v in default_ratio.items()}
    survey['fiducial'].add_field(tier, depths_mag = depths_mag, area = 1)



# --- GLASS
survey['GLASS'] = Survey('GLASS', depth_reference_filter = 'JWST/NIRCam.F150W')
survey['GLASS'].add_field('Abell-2744-Parallel', depths_mag = {'JWST/NIRCam.F090W': 29.21, 'JWST/NIRCam.F115W': 29.4, 'JWST/NIRCam.F150W': 29.26,  'JWST/NIRCam.F200W': 29.41, 'JWST/NIRCam.F277W': 29.03,  'JWST/NIRCam.F356W': 29.15,  'JWST/NIRCam.F444W': 29.46}, area = 10) # based on JT's calculations

# --- UNCOVER
# survey['UNCOVER'] = Survey('UNCOVER')
# survey['UNCOVER'].add_field('Abell 2744 Parallel', depths_mag = {'JWST/NIRCam.F090W': 29.21, 'JWST/NIRCam.F115W': 29.4, 'JWST/NIRCam.F150W': 29.26,  'JWST/NIRCam.F200W': 29.41, 'JWST/NIRCam.F277W': 29.03,  'JWST/NIRCam.F356W': 29.15,  'JWST/NIRCam.F444W': 29.46}, area = 10, depth_reference_filter = 'JWST/NIRCam.F150W')


# --- JADES
survey['JADES'] = Survey('JADES', depth_reference_filter = 'JWST/NIRCam.F150W')
survey['JADES'].add_field('deep', depths_mag = {'JWST/NIRCam.F150W': 30.7,  'JWST/NIRCam.F277W': 30.7, 'JWST/NIRCam.F200W': 30.7, 'JWST/NIRCam.F356W': 30.2}, area = 46)
survey['JADES'].add_field('medium', depths_mag = {'JWST/NIRCam.F150W': 29.7, 'JWST/NIRCam.F277W': 29.8, 'JWST/NIRCam.F200W': 29.8, 'JWST/NIRCam.F356W': 29.4}, area = 144)



# --- CEERS
survey['CEERS'] = Survey('CEERS', depth_reference_filter = 'JWST/NIRCam.F150W')
survey['CEERS'].add_field('Epoch-1', depths_mag = {'JWST/NIRCam.F115W': 29.0, 'JWST/NIRCam.F150W': 28.9, 'JWST/NIRCam.F200W': 28.95, 'JWST/NIRCam.F277W': 28.95, 'JWST/NIRCam.F356W': 28.95, 'JWST/NIRCam.F444W': 28.3}, area = 4.*9.1)
survey['CEERS'].add_field('Epoch-2', depths_mag = {'JWST/NIRCam.F115W': 29.0, 'JWST/NIRCam.F150W': 28.9, 'JWST/NIRCam.F200W': 28.95, 'JWST/NIRCam.F277W': 28.95, 'JWST/NIRCam.F356W': 28.95, 'JWST/NIRCam.F444W': 28.3}, area = 6.*9.1)

# --- CEERS-June
survey['CEERS-June'] = Survey('CEERS-June', depth_reference_filter = 'JWST/NIRCam.F150W')
survey['CEERS-June'].add_field('Epoch-1', depths_mag = {'JWST/NIRCam.F115W': 29.0, 'JWST/NIRCam.F150W': 28.9, 'JWST/NIRCam.F200W': 28.95, 'JWST/NIRCam.F277W': 28.95, 'JWST/NIRCam.F356W': 28.95, 'JWST/NIRCam.F444W': 28.3}, area = 4.*9.1)

# --- PEARLS
survey['PEARLS'] = Survey('PEARLS', depth_reference_filter = 'JWST/NIRCam.F150W')

nep_depths = {'JWST/NIRCam.F090W': 28.4, 'JWST/NIRCam.F115W': 28.6, 'JWST/NIRCam.F150W': 28.8, 'JWST/NIRCam.F200W': 28.9, 'JWST/NIRCam.F277W': 28.5, 'JWST/NIRCam.F356W': 28.5, 'JWST/NIRCam.F410M': 27.7}

survey['PEARLS'].add_field('NEP', depths_mag = nep_depths, area = 47)
survey['PEARLS'].add_field('NEP-overlap', depths_mag = {k:v+0.75 for k, v in nep_depths.items()}, area = 8.324)
survey['PEARLS'].add_field('IDF', depths_mag = {'JWST/NIRCam.F150W': 28.98, 'JWST/NIRCam.F200W': 29.16, 'JWST/NIRCam.F356W': 28.83, 'JWST/NIRCam.F444W': 28.43}, area = 9.1) # based on JT's calculations
survey['PEARLS'].add_field('ERS', depths_mag = {k:v-0.75 for k, v in nep_depths.items()}, area = 8.324)




# PEARLS.add_field('IDF', depths_mag = {'JWST/NIRCam.F090W': 28.4, 'JWST/NIRCam.F115W': 28.6, 'JWST/NIRCam.F150W': 28.8, 'JWST/NIRCam.F200W': 28.9, 'JWST/NIRCam.F277W': 28.5, 'JWST/NIRCam.F356W': 28.5, 'JWST/NIRCam.F410M': 27.7, 'JWST/NIRCam.F444W': 28.00}, area = 9.1, depth_reference_filter = 'JWST/NIRCam.F150W')
# PEARLS.add_field('ERS', depths_mag = {'JWST/NIRCam.F090W': 28.4, 'JWST/NIRCam.F115W': 28.6, 'JWST/NIRCam.F150W': 28.8, 'JWST/NIRCam.F200W': 28.9, 'JWST/NIRCam.F277W': 28.5, 'JWST/NIRCam.F356W': 28.5, 'JWST/NIRCam.F410M': 27.7, 'JWST/NIRCam.F444W': 28.00}, area = 9.1, depth_reference_filter = 'JWST/NIRCam.F150W')

# --- COSMOS-Web [5\sigma, 0".15]
survey['COSMOS-Web'] = Survey('COSMOS-Web', depth_reference_filter = 'JWST/NIRCam.F150W')
survey['COSMOS-Web'].add_field('1', depths_mag = {'Hubble.ACS.f814w': 27.2, 'JWST/NIRCam.F115W': 26.64, 'JWST/NIRCam.F150W': 26.95, 'JWST/NIRCam.F277W': 27.61, 'JWST/NIRCam.F444W': 27.49}, area = 19.0)
survey['COSMOS-Web'].add_field('2', depths_mag = {'Hubble.ACS.f814w': 27.2, 'JWST/NIRCam.F115W': 27.01, 'JWST/NIRCam.F150W': 27.31, 'JWST/NIRCam.F277W': 27.93, 'JWST/NIRCam.F444W': 27.83}, area = 980.0)
survey['COSMOS-Web'].add_field('3', depths_mag = {'Hubble.ACS.f814w': 27.2, 'JWST/NIRCam.F115W': 27.21, 'JWST/NIRCam.F150W': 27.51, 'JWST/NIRCam.F277W': 28.11, 'JWST/NIRCam.F444W': 27.96}, area = 21.6)
survey['COSMOS-Web'].add_field('4', depths_mag = {'Hubble.ACS.f814w': 27.2, 'JWST/NIRCam.F115W': 27.52, 'JWST/NIRCam.F150W': 27.67, 'JWST/NIRCam.F277W': 28.24, 'JWST/NIRCam.F444W': 28.17 }, area = 904.9)

# --- PRIMER
survey['PRIMER'] = Survey('PRIMER', depth_reference_filter = 'JWST/NIRCam.F150W')
survey['PRIMER'].add_field('COSMOS-Shallow', depths_mag = {'JWST/NIRCam.F090W': 28.33 ,'JWST/NIRCam.F115W': 28.61, 'JWST/NIRCam.F150W': 28.81, 'JWST/NIRCam.F200W': 28.89, 'JWST/NIRCam.F277W': 28.85, 'JWST/NIRCam.F356W': 28.79, 'JWST/NIRCam.F410M': 28.04, 'JWST/NIRCam.F444W': 28.32}, area = 144.2)
survey['PRIMER'].add_field('COSMOS-Medium', depths_mag = {'JWST/NIRCam.F090W': 28.57,'JWST/NIRCam.F115W': 28.84, 'JWST/NIRCam.F150W': 29.03, 'JWST/NIRCam.F200W': 29.11, 'JWST/NIRCam.F277W': 29.08, 'JWST/NIRCam.F356W': 29.02, 'JWST/NIRCam.F410M': 28.27, 'JWST/NIRCam.F444W': 28.54}, area = 108.3)
survey['PRIMER'].add_field('COSMOS-Deep', depths_mag = {'JWST/NIRCam.F090W': 28.96,'JWST/NIRCam.F115W': 29.23, 'JWST/NIRCam.F150W': 29.43, 'JWST/NIRCam.F200W': 29.51, 'JWST/NIRCam.F277W': 29.47, 'JWST/NIRCam.F356W': 29.42, 'JWST/NIRCam.F410M': 28.65, 'JWST/NIRCam.F444W': 28.93}, area = 33.4)
survey['PRIMER'].add_field('UDS-Shallow', depths_mag = {'JWST/NIRCam.F090W': 27.92,'JWST/NIRCam.F115W': 28.21, 'JWST/NIRCam.F150W': 28.42, 'JWST/NIRCam.F200W': 28.48, 'JWST/NIRCam.F277W': 28.38, 'JWST/NIRCam.F356W': 28.37, 'JWST/NIRCam.F410M': 27.57, 'JWST/NIRCam.F444W': 27.79}, area =  234.02)
survey['PRIMER'].add_field('UDS-Medium', depths_mag = {'JWST/NIRCam.F090W': 28.32,'JWST/NIRCam.F115W': 28.62, 'JWST/NIRCam.F150W': 28.82, 'JWST/NIRCam.F200W': 28.69, 'JWST/NIRCam.F277W': 28.85, 'JWST/NIRCam.F356W': 28.77, 'JWST/NIRCam.F410M': 27.97, 'JWST/NIRCam.F444W': 28.21}, area = 175.17)


survey['PRIMER-July'] = Survey('PRIMER-July', depth_reference_filter = 'JWST/NIRCam.F150W')
survey['PRIMER-July'].add_field('UDS-Shallow', depths_mag = {'JWST/NIRCam.F090W': 27.92,'JWST/NIRCam.F115W': 28.21, 'JWST/NIRCam.F150W': 28.42, 'JWST/NIRCam.F200W': 28.48, 'JWST/NIRCam.F277W': 28.38, 'JWST/NIRCam.F356W': 28.37, 'JWST/NIRCam.F410M': 27.57, 'JWST/NIRCam.F444W': 27.79}, area =  3*9.1)


# --- NGDEEP
survey['NGDEEP'] = Survey('NGDEEP', depth_reference_filter = 'JWST/NIRCam.F150W')
survey['NGDEEP'].add_field('', depths_mag = {'JWST/NIRCam.F115W': 30.90, 'JWST/NIRCam.F150W': 30.62, 'JWST/NIRCam.F200W': 30.62, 'JWST/NIRCam.F277W': 30.72, 'JWST/NIRCam.F356W': 30.70, 'JWST/NIRCam.F444W': 30.56}, area = 2*9.1)

# survey['NGDEEP'] = Survey('NGDEEP')
# survey['NGDEEP'].add_field('', depths_mag = {'JWST/NIRCam.F115W': 31.01, 'JWST/NIRCam.F150W': 30.78, 'JWST/NIRCam.F200W': 30.81, 'JWST/NIRCam.F277W': 30.56, 'JWST/NIRCam.F356W': 30.54, 'JWST/NIRCam.F444W': 30.47}, area = 2*9.1, depth_reference_filter = 'JWST/NIRCam.F150W') # based on JT's calculations




# --- PANORAMIC
survey['PANORAMIC'] = Survey('PANORAMIC', depth_reference_filter = 'JWST/NIRCam.F150W')
survey['PANORAMIC'].add_field('0', area = 20.4, depths_mag = {'JWST/NIRCam.F150W': 29.64 ,'JWST/NIRCam.F277W': 29.64 })
survey['PANORAMIC'].add_field('1', area = 13.6, depths_mag = {'JWST/NIRCam.F150W': 29.63 ,'JWST/NIRCam.F277W': 29.63 })
survey['PANORAMIC'].add_field('2', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.58 ,'JWST/NIRCam.F277W': 29.58 })
survey['PANORAMIC'].add_field('3', area = 20.4, depths_mag = {'JWST/NIRCam.F150W': 29.55 ,'JWST/NIRCam.F277W': 29.55 })
survey['PANORAMIC'].add_field('4', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.53 ,'JWST/NIRCam.F277W': 29.53 })
survey['PANORAMIC'].add_field('6', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.47 ,'JWST/NIRCam.F277W': 29.47 })
survey['PANORAMIC'].add_field('7', area = 13.6, depths_mag = {'JWST/NIRCam.F150W': 29.45 ,'JWST/NIRCam.F277W': 29.45 })
survey['PANORAMIC'].add_field('8', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.42 ,'JWST/NIRCam.F277W': 29.42 })
survey['PANORAMIC'].add_field('9', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.4 ,'JWST/NIRCam.F277W': 29.4 })
survey['PANORAMIC'].add_field('10', area = 13.6, depths_mag = {'JWST/NIRCam.F150W': 29.34 ,'JWST/NIRCam.F277W': 29.34 })
survey['PANORAMIC'].add_field('11', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.32 ,'JWST/NIRCam.F277W': 29.32 })
survey['PANORAMIC'].add_field('12', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.25 ,'JWST/NIRCam.F277W': 29.25 })
survey['PANORAMIC'].add_field('13', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.22 ,'JWST/NIRCam.F277W': 29.22 })
survey['PANORAMIC'].add_field('14', area = 27.2, depths_mag = {'JWST/NIRCam.F150W': 29.16 ,'JWST/NIRCam.F277W': 29.16 })
survey['PANORAMIC'].add_field('15', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.13 ,'JWST/NIRCam.F277W': 29.13 })
survey['PANORAMIC'].add_field('16', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 29.07 ,'JWST/NIRCam.F277W': 29.07 })
survey['PANORAMIC'].add_field('17', area = 6.8, depths_mag = {'JWST/NIRCam.F150W': 28.99 ,'JWST/NIRCam.F277W': 28.99 })
survey['PANORAMIC'].add_field('18', area = 95.2, depths_mag = {'JWST/NIRCam.F150W': 28.95 ,'JWST/NIRCam.F277W': 28.95 })
survey['PANORAMIC'].add_field('19', area = 34.0, depths_mag = {'JWST/NIRCam.F150W': 28.91 ,'JWST/NIRCam.F277W': 28.91 })
survey['PANORAMIC'].add_field('20', area = 54.3, depths_mag = {'JWST/NIRCam.F150W': 28.86 ,'JWST/NIRCam.F277W': 28.86 })
survey['PANORAMIC'].add_field('21', area = 74.8, depths_mag = {'JWST/NIRCam.F150W': 28.8 ,'JWST/NIRCam.F277W': 28.8 })
survey['PANORAMIC'].add_field('22', area = 54.4, depths_mag = {'JWST/NIRCam.F150W': 28.74 ,'JWST/NIRCam.F277W': 28.74 })
survey['PANORAMIC'].add_field('23', area = 68.0, depths_mag = {'JWST/NIRCam.F150W': 28.67 ,'JWST/NIRCam.F277W': 28.67 })
survey['PANORAMIC'].add_field('24', area = 27.2, depths_mag = {'JWST/NIRCam.F150W': 28.6 ,'JWST/NIRCam.F277W': 28.6 })
survey['PANORAMIC'].add_field('25', area = 54.4, depths_mag = {'JWST/NIRCam.F150W': 28.51 ,'JWST/NIRCam.F277W': 28.51 })
survey['PANORAMIC'].add_field('26', area = 272.0, depths_mag = {'JWST/NIRCam.F150W': 28.4 ,'JWST/NIRCam.F277W': 28.4 })
survey['PANORAMIC'].add_field('27', area = 380.7, depths_mag = {'JWST/NIRCam.F150W': 28.26 ,'JWST/NIRCam.F277W': 28.26 })
survey['PANORAMIC'].add_field('28', area = 149.6, depths_mag = {'JWST/NIRCam.F150W': 27.96 ,'JWST/NIRCam.F277W': 27.96 })




# .add_field('', depths_mag = , area = , depth_reference_filter = 'JWST/NIRCam.F150W')


# --- lists of surveys
surveys = {}
surveys['Public Cycle 1'] = [survey['GLASS'], survey['NGDEEP'], survey['PEARLS'], survey['CEERS'], survey['PRIMER'], survey['PANORAMIC'], survey['COSMOS-Web']]
Cy1_ = surveys['Cycle-1'] = surveys['Cycle 1'] = surveys['Public Cycle 1'] + [survey['JADES']]




survey['Public Cycle 1'] = combine_surveys('Public Cycle 1', surveys['Public Cycle 1'])
Cy1 = survey['Cycle-1'] = survey['Cycle 1'] = combine_surveys('Cycle-1', surveys['Cycle-1'])

# surveys['Nov22'] = [survey['PEARLS'], survey['CEERS-June'], survey['PRIMER-July']]
# survey['Nov22'] = combine_surveys('Nov22', surveys['Nov22'])


# --- make a sub-survey using a sub-set of fields

Nov22_ = ['GLASS/Abell-2744-Parallel', 'CEERS/Epoch-1', 'PEARLS/IDF', 'PEARLS/NEP']
Nov22 = survey['Nov22'] = combine_fields('FLAGS.DR1', survey, Nov22_) # approximate

# survey['FLAGS-DR1'] = combine_fields('FLAGS.DR1', survey, ['GLASS/Abell-2744-Parallel', 'CEERS/Epoch-1'])

# surveys['JADES'] = JADES
