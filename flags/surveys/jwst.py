
from .utils import Survey, combine_surveys

survey = {}

# --- JADES
survey['JADES'] = Survey('JADES')
survey['JADES'].add_field('deep', depths_mag = {'Webb.NIRCAM.F150W': 30.7,  'Webb.NIRCAM.F277W': 30.7, 'Webb.NIRCAM.F200W': 30.7, 'Webb.NIRCAM.F356W': 30.2}, area = 46, depth_reference_filter = 'Webb.NIRCAM.F150W')
survey['JADES'].add_field('medium', depths_mag = {'Webb.NIRCAM.F150W': 29.7, 'Webb.NIRCAM.F277W': 29.8, 'Webb.NIRCAM.F200W': 29.8, 'Webb.NIRCAM.F356W': 29.4}, area = 144, depth_reference_filter = 'Webb.NIRCAM.F150W')

# --- CEERS
survey['CEERS'] = Survey('CEERS')
survey['CEERS'].add_field('1', depths_mag = {'Webb.NIRCAM.F150W': 28.9, 'Webb.NIRCAM.F200W': 28.95, 'Webb.NIRCAM.F277W': 28.95, 'Webb.NIRCAM.F356W': 28.95}, area = 10.*9.1, depth_reference_filter = 'Webb.NIRCAM.F150W')

# --- PEARLS
survey['PEARLS'] = Survey('PEARLS')
survey['PEARLS'].add_field('NEP', depths_mag = {'Webb.NIRCAM.F090W': 28.4, 'Webb.NIRCAM.F115W': 28.6, 'Webb.NIRCAM.F150W': 28.8, 'Webb.NIRCAM.F200W': 28.9, 'Webb.NIRCAM.F277W': 28.5, 'Webb.NIRCAM.F356W': 28.5, 'Webb.NIRCAM.F410M': 27.7, 'Webb.NIRCAM.F444W': 28.00}, area = 54.7, depth_reference_filter = 'Webb.NIRCAM.F150W')
# PEARLS.add_field('IDF', depths_mag = {'Webb.NIRCAM.F090W': 28.4, 'Webb.NIRCAM.F115W': 28.6, 'Webb.NIRCAM.F150W': 28.8, 'Webb.NIRCAM.F200W': 28.9, 'Webb.NIRCAM.F277W': 28.5, 'Webb.NIRCAM.F356W': 28.5, 'Webb.NIRCAM.F410M': 27.7, 'Webb.NIRCAM.F444W': 28.00}, area = 9.1, depth_reference_filter = 'Webb.NIRCAM.F150W')
# PEARLS.add_field('ERS', depths_mag = {'Webb.NIRCAM.F090W': 28.4, 'Webb.NIRCAM.F115W': 28.6, 'Webb.NIRCAM.F150W': 28.8, 'Webb.NIRCAM.F200W': 28.9, 'Webb.NIRCAM.F277W': 28.5, 'Webb.NIRCAM.F356W': 28.5, 'Webb.NIRCAM.F410M': 27.7, 'Webb.NIRCAM.F444W': 28.00}, area = 9.1, depth_reference_filter = 'Webb.NIRCAM.F150W')

# --- COSMOS-Web
survey['COSMOS_Web'] = Survey('COSMOS-Web')
survey['COSMOS_Web'].add_field('1', depths_mag = {'Hubble.ACS.f814w': 27.2, 'Webb.NIRCAM.F115W': 26.74, 'Webb.NIRCAM.F150W': 26.99, 'Webb.NIRCAM.F277W': 27.43, 'Webb.NIRCAM.F444W': 27.10}, area = 96, depth_reference_filter = 'Webb.NIRCAM.F150W')
survey['COSMOS_Web'].add_field('2', depths_mag = {'Hubble.ACS.f814w': 27.2, 'Webb.NIRCAM.F115W': 27.13, 'Webb.NIRCAM.F150W': 27.38, 'Webb.NIRCAM.F277W': 27.82, 'Webb.NIRCAM.F444W': 27.49}, area = 1071, depth_reference_filter = 'Webb.NIRCAM.F150W')
survey['COSMOS_Web'].add_field('3', depths_mag = {'Hubble.ACS.f814w': 27.2, 'Webb.NIRCAM.F115W': 27.36, 'Webb.NIRCAM.F150W': 27.61, 'Webb.NIRCAM.F277W': 28.05, 'Webb.NIRCAM.F444W': 27.72}, area = 41, depth_reference_filter = 'Webb.NIRCAM.F150W')
survey['COSMOS_Web'].add_field('4', depths_mag = {'Hubble.ACS.f814w': 27.2, 'Webb.NIRCAM.F115W': 27.52, 'Webb.NIRCAM.F150W': 27.77, 'Webb.NIRCAM.F277W': 28.21 }, area = 753, depth_reference_filter = 'Webb.NIRCAM.F150W')

# --- PRIMER
survey['PRIMER'] = Survey('PRIMER')
survey['PRIMER'].add_field('COSMOS-Shallow', depths_mag = {'Webb.NIRCAM.F090W': 28.33 ,'Webb.NIRCAM.F115W': 28.61, 'Webb.NIRCAM.F150W': 28.81, 'Webb.NIRCAM.F200W': 28.89, 'Webb.NIRCAM.F277W': 28.85, 'Webb.NIRCAM.F356W': 28.79, 'Webb.NIRCAM.F410M': 28.04, 'Webb.NIRCAM.F444W': 28.32}, area = 144.2, depth_reference_filter = 'Webb.NIRCAM.F150W')
survey['PRIMER'].add_field('COSMOS-Medium', depths_mag = {'Webb.NIRCAM.F090W': 28.57,'Webb.NIRCAM.F115W': 28.84, 'Webb.NIRCAM.F150W': 29.03, 'Webb.NIRCAM.F200W': 29.11, 'Webb.NIRCAM.F277W': 29.08, 'Webb.NIRCAM.F356W': 29.02, 'Webb.NIRCAM.F410M': 28.27, 'Webb.NIRCAM.F444W': 28.54}, area = 108.3, depth_reference_filter = 'Webb.NIRCAM.F150W')
survey['PRIMER'].add_field('COSMOS-Deep', depths_mag = {'Webb.NIRCAM.F090W': 28.96,'Webb.NIRCAM.F115W': 29.23, 'Webb.NIRCAM.F150W': 29.43, 'Webb.NIRCAM.F200W': 29.51, 'Webb.NIRCAM.F277W': 29.47, 'Webb.NIRCAM.F356W': 29.42, 'Webb.NIRCAM.F410M': 28.65, 'Webb.NIRCAM.F444W': 28.93}, area = 33.4, depth_reference_filter = 'Webb.NIRCAM.F150W')
survey['PRIMER'].add_field('UDS-Shallow', depths_mag = {'Webb.NIRCAM.F090W': 27.92,'Webb.NIRCAM.F115W': 28.21, 'Webb.NIRCAM.F150W': 28.42, 'Webb.NIRCAM.F200W': 28.48, 'Webb.NIRCAM.F277W': 28.38, 'Webb.NIRCAM.F356W': 28.37, 'Webb.NIRCAM.F410M': 27.57, 'Webb.NIRCAM.F444W': 27.79}, area =  234.02, depth_reference_filter = 'Webb.NIRCAM.F150W')
survey['PRIMER'].add_field('UDS-Medium', depths_mag = {'Webb.NIRCAM.F090W': 28.32,'Webb.NIRCAM.F115W': 28.62, 'Webb.NIRCAM.F150W': 28.82, 'Webb.NIRCAM.F200W': 28.69, 'Webb.NIRCAM.F277W': 28.85, 'Webb.NIRCAM.F356W': 28.77, 'Webb.NIRCAM.F410M': 27.97, 'Webb.NIRCAM.F444W': 28.21}, area = 175.17, depth_reference_filter = 'Webb.NIRCAM.F150W')

# --- NGDEEP
survey['NGDEEP'] = Survey('NGDEEP')
survey['NGDEEP'].add_field('', depths_mag = {'Webb.NIRCAM.F115W': 30.90, 'Webb.NIRCAM.F150W': 30.62, 'Webb.NIRCAM.F200W': 30.62, 'Webb.NIRCAM.F277W': 30.72, 'Webb.NIRCAM.F356W': 30.70, 'Webb.NIRCAM.F444W': 30.56}, area = 2*9.1, depth_reference_filter = 'Webb.NIRCAM.F150W')

# --- PANORAMIC
survey['PANORAMIC'] = Survey('PANORAMIC')
survey['PANORAMIC'].add_field('0', area = 20.4, depths_mag = {'Webb.NIRCAM.F150W': 29.64 ,'Webb.NIRCAM.F277W': 29.64 })
survey['PANORAMIC'].add_field('1', area = 13.6, depths_mag = {'Webb.NIRCAM.F150W': 29.63 ,'Webb.NIRCAM.F277W': 29.63 })
survey['PANORAMIC'].add_field('2', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.58 ,'Webb.NIRCAM.F277W': 29.58 })
survey['PANORAMIC'].add_field('3', area = 20.4, depths_mag = {'Webb.NIRCAM.F150W': 29.55 ,'Webb.NIRCAM.F277W': 29.55 })
survey['PANORAMIC'].add_field('4', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.53 ,'Webb.NIRCAM.F277W': 29.53 })
survey['PANORAMIC'].add_field('6', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.47 ,'Webb.NIRCAM.F277W': 29.47 })
survey['PANORAMIC'].add_field('7', area = 13.6, depths_mag = {'Webb.NIRCAM.F150W': 29.45 ,'Webb.NIRCAM.F277W': 29.45 })
survey['PANORAMIC'].add_field('8', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.42 ,'Webb.NIRCAM.F277W': 29.42 })
survey['PANORAMIC'].add_field('9', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.4 ,'Webb.NIRCAM.F277W': 29.4 })
survey['PANORAMIC'].add_field('10', area = 13.6, depths_mag = {'Webb.NIRCAM.F150W': 29.34 ,'Webb.NIRCAM.F277W': 29.34 })
survey['PANORAMIC'].add_field('11', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.32 ,'Webb.NIRCAM.F277W': 29.32 })
survey['PANORAMIC'].add_field('12', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.25 ,'Webb.NIRCAM.F277W': 29.25 })
survey['PANORAMIC'].add_field('13', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.22 ,'Webb.NIRCAM.F277W': 29.22 })
survey['PANORAMIC'].add_field('14', area = 27.2, depths_mag = {'Webb.NIRCAM.F150W': 29.16 ,'Webb.NIRCAM.F277W': 29.16 })
survey['PANORAMIC'].add_field('15', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.13 ,'Webb.NIRCAM.F277W': 29.13 })
survey['PANORAMIC'].add_field('16', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 29.07 ,'Webb.NIRCAM.F277W': 29.07 })
survey['PANORAMIC'].add_field('17', area = 6.8, depths_mag = {'Webb.NIRCAM.F150W': 28.99 ,'Webb.NIRCAM.F277W': 28.99 })
survey['PANORAMIC'].add_field('18', area = 95.2, depths_mag = {'Webb.NIRCAM.F150W': 28.95 ,'Webb.NIRCAM.F277W': 28.95 })
survey['PANORAMIC'].add_field('19', area = 34.0, depths_mag = {'Webb.NIRCAM.F150W': 28.91 ,'Webb.NIRCAM.F277W': 28.91 })
survey['PANORAMIC'].add_field('20', area = 54.3, depths_mag = {'Webb.NIRCAM.F150W': 28.86 ,'Webb.NIRCAM.F277W': 28.86 })
survey['PANORAMIC'].add_field('21', area = 74.8, depths_mag = {'Webb.NIRCAM.F150W': 28.8 ,'Webb.NIRCAM.F277W': 28.8 })
survey['PANORAMIC'].add_field('22', area = 54.4, depths_mag = {'Webb.NIRCAM.F150W': 28.74 ,'Webb.NIRCAM.F277W': 28.74 })
survey['PANORAMIC'].add_field('23', area = 68.0, depths_mag = {'Webb.NIRCAM.F150W': 28.67 ,'Webb.NIRCAM.F277W': 28.67 })
survey['PANORAMIC'].add_field('24', area = 27.2, depths_mag = {'Webb.NIRCAM.F150W': 28.6 ,'Webb.NIRCAM.F277W': 28.6 })
survey['PANORAMIC'].add_field('25', area = 54.4, depths_mag = {'Webb.NIRCAM.F150W': 28.51 ,'Webb.NIRCAM.F277W': 28.51 })
survey['PANORAMIC'].add_field('26', area = 272.0, depths_mag = {'Webb.NIRCAM.F150W': 28.4 ,'Webb.NIRCAM.F277W': 28.4 })
survey['PANORAMIC'].add_field('27', area = 380.7, depths_mag = {'Webb.NIRCAM.F150W': 28.26 ,'Webb.NIRCAM.F277W': 28.26 })
survey['PANORAMIC'].add_field('28', area = 149.6, depths_mag = {'Webb.NIRCAM.F150W': 27.96 ,'Webb.NIRCAM.F277W': 27.96 })




# .add_field('', depths_mag = , area = , depth_reference_filter = 'Webb.NIRCAM.F150W')


# --- lists of surveys
surveys = {}
# surveys['Public Cy1'] = [CEERS, PEARLS, COSMOS_Web, PRIMER, NGDEEP, PANORAMIC]
# surveys['Complete Cycle 1'] = surveys['Public Cy1'] + [JADES]
#
# PublicCy1 = combine_surveys('Public Cy1', surveys['Public Cy1'])
# Cy1 = combine_surveys('Complete Cycle 1', surveys['Complete Cycle 1'])




# surveys['JADES'] = JADES
