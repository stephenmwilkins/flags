
import numpy as np
from .utils import Survey, combine_surveys, combine_fields

survey = {}


# --- Euclid

filters = ['Euclid/VIS.VIS'] + [f'Euclid/NISP.{f}' for f in ['Y','J','H']]


s = Survey('Euclid-deep', depth_reference_filter = 'Euclid/NISP.H')
s.add_field('', filters = filters, depths_mag = {'Euclid/VIS.VIS': 26, 'Euclid/NISP.Y': 26, 'Euclid/NISP.J': 26, 'Euclid/NISP.H': 26}, area = 40*3600)
survey['Euclid-deep'] = s

s = Survey('Euclid-wide', depth_reference_filter = 'Euclid/NISP.H')
s.add_field('', filters = filters, depths_mag = {'Euclid/VIS.VIS': 24, 'Euclid/NISP.Y': 24, 'Euclid/NISP.J': 24, 'Euclid/NISP.H': 24}, area = 15000*3600)
survey['Euclid-wide'] = s


AllEuclid_ = [survey['Euclid-wide'], survey['Euclid-deep']]

AllEuclid = combine_surveys('AllEuclid', AllEuclid_)
