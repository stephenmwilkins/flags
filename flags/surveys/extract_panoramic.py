

import numpy as np


depth, cumarea = np.loadtxt('data/PANORAMIC_expected_depth_area_vMarch2022.txt', usecols = (0,1), unpack = True)

print(depth, cumarea)

prearea = np.insert(cumarea[0:-1], 0, 0.0)

print(prearea)

area = cumarea - prearea

for i, (d, a) in enumerate(zip(depth, area)):

    # print(i, d, a)

    print(f"PANORAMIC.add_field('{i}', area = {a:.1f}, depths_mag = {{'Webb.NIRCam.F150W': {d} ,'Webb.NIRCam.F277W': {d} }})")
