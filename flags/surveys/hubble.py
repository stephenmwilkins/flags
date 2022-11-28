
import numpy as np
from .utils import Survey, combine_surveys, combine_fields

survey = {}


filters = ['Hubble.WFC3.F160W']

s = Survey('HUDF09', depth_reference_filter = 'Hubble.WFC3.F160W')
s.add_field('XDF', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 29.4}, area = 4.7)
s.add_field('HUDF09-1', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 28.3}, area = 4.7)
s.add_field('HUDF09-2', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 28.7}, area = 4.7)
survey['HUDF09'] = s

s = Survey('ERS', depth_reference_filter = 'Hubble.WFC3.F160W')
s.add_field('ERS', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 27.4}, area = 40.5)
survey['ERS'] = s

s = Survey('CANDELS', depth_reference_filter = 'Hubble.WFC3.F160W')
s.add_field('CANDELS-GS-DEEP', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 27.5}, area = 64.5)
s.add_field('CANDELS-GS-WIDE', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 26.8}, area = 34.2)
s.add_field('CANDELS-GN-DEEP', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 27.5}, area = 62.9)
s.add_field('CANDELS-GN-WIDE', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 26.7}, area = 60.9)
s.add_field('CANDELS-UDS', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 26.8}, area = 151.2)
s.add_field('CANDELS-EGS', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 26.9}, area = 150.7)
s.add_field('CANDELS-COSMOS', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 26.8}, area = 151.9)
survey['CANDELS'] = s


s = Survey('BORG', depth_reference_filter = 'Hubble.WFC3.F160W')
s.add_field('BORG', filters = filters, depths_mag = {'Hubble.WFC3.F160W': 27}, area = 218.3)
survey['BORG'] = s


AllHubble_ = [survey['HUDF09'], survey['ERS'], survey['CANDELS'], survey['BORG']]

AllHubble = combine_surveys('AllHubble', AllHubble_)
