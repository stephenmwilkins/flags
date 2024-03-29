

import copy

import numpy as np

class empty: pass

import flare
import flare.filters
import flare.observatories
import flare.photom

from flare.photom import flux_to_m

class Survey:

    def __init__(self, name, depth_reference_filter = None):

        self.name = name
        self.depth_reference_filter = depth_reference_filter
        self.fields = {}
        self.fields_ = []

    def add_field(self, field_name, data_dir = None, data_reference = None, filters = None, depths_flux = None, depths_mag = None, area = None, mask_file = None, depth_aperture_radius_arcsec = None, depth_aperture_radius_pixel = None, depth_aperture_significance = 5, pixel_scale = None, detection_filters = None, depth_reference_filter = None):

        if not depth_reference_filter:
            depth_reference_filter = self.depth_reference_filter

        if depths_flux:
            depths_mag = {f: flare.photom.flux_to_m(m) for f, m in depths.items()}
        else:
            depths_flux = {f: flare.photom.m_to_flux(m) for f, m in depths_mag.items()}

        noise_flux = {f: flux/depth_aperture_significance for f, flux in depths_flux.items()}
        noise_mag = {f: mag + 2.5*np.log10(depth_aperture_significance) for f, mag in depths_mag.items()}

        filters = list(depths_flux.keys())

        field = {'name': field_name, 'depths_mag': depths_mag, 'depths_flux': depths_flux, 'area': area, 'filters': filters, 'noise_flux': noise_flux, 'noise_mag': noise_mag, 'depth_reference_filter': depth_reference_filter}
        self.fields[field_name] = field
        self.fields_.append(field)


    def get_cumulative_area(self):



        fields = sorted(self.fields_ , key=lambda k: k['depths_mag'][k['depth_reference_filter']])[::-1]

        cumulative_area = 1E-10
        x = []
        y = []
        for field in fields:
            depth = field['depths_mag'][field['depth_reference_filter']]
            y.append(cumulative_area)
            x.append(depth+0.0001) # the nudge is needed for the interpolation
            cumulative_area += field['area']/3600.
            y.append(cumulative_area)
            x.append(depth)
        y.append(cumulative_area)
        x.append(0)

        return x, y



def combine_surveys(name, surveys):

    survey = Survey(name, depth_reference_filter = surveys[0].depth_reference_filter)

    for s in surveys:

        for fn, f in s.fields.items():

            survey.fields[f'{s.name}/{fn}'] = f

    survey.fields_ = list(survey.fields.values())

    return survey


def combine_fields(name, surveys, field_list):

    survey = Survey(name)

    for i in field_list:
        survey_name, field_name = i.split('/')
        f = surveys[survey_name].fields[field_name]
        f['name'] = i
        survey.fields[f'{survey_name}/{field_name}'] = f

    survey.fields_ = list(survey.fields.values())

    return survey
