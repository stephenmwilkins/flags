
import numpy as np
from .utils import Survey, combine_surveys, combine_fields

survey = {}

filters = ['Paranal/VISTA.Z','Paranal/VISTA.Y','Paranal/VISTA.J','Paranal/VISTA.H','Paranal/VISTA.Ks']

s = Survey('UltraVISTA', depth_reference_filter = 'Paranal/VISTA.H')
s.add_field('deep', filters = filters, depths_mag = {'Paranal/VISTA.H': 25.26}, area = 0.9*3600.) # from Donnan '22
s.add_field('ultra-deep', filters = filters, depths_mag = {'Paranal/VISTA.H': 24.96}, area = 0.9*3600.) # from Donnan '22
survey['UltraVISTA'] = s

s = Survey('VIDEO', depth_reference_filter = 'Paranal/VISTA.H')
s.add_field('', filters = filters, depths_mag = {'Paranal/VISTA.H': 24.0}, area = 12*3600.) # from Donnan '22
survey['VIDEO'] = s

s = Survey('VIKING', depth_reference_filter = 'Paranal/VISTA.H')
s.add_field('', filters = filters, depths_mag = {'Paranal/VISTA.H': 21.5}, area = 1500*3600.) # from Donnan '22
survey['VIKING'] = s

s = Survey('VHS', depth_reference_filter = 'Paranal/VISTA.H')
s.add_field('', filters = filters, depths_mag = {'Paranal/VISTA.H': 20.6}, area = 20000*3600.) # from Donnan '22
survey['VHS'] = s

AllVISTA_ = [survey['UltraVISTA'],survey['VIDEO'],survey['VIKING'],survey['VHS']]

AllVISTA = combine_surveys('AllVISTA', AllVISTA_)
