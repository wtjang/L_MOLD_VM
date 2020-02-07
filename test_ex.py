# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:12:29 2020

@author: wtjang
"""


from wafer_map import wm_app




data = [(0,0, 1969.493), 
        (0,95,2014.453),
        (-67.1751,	67.1751,	1000),
        (-95,	0,	2015.6959),
        (-67.1751,	-67.1751,	2014.524),
        (0	,-95,	2014.9785),
        (67.1751,	-67.1751,	2041.684),
        (95,	0,	2043.2437),
        (67.1751,	67.1751,2041.6567)
        ]





wm_app.WaferMapApp(data, (1,1),(0,0),150)

import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt

data_1 = np.array([[ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ],
       [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
       [ 1. ,  2. ,  0.1,  2. ,  2. ,  1. ],
       [ 1. ,  2. ,  2. ,  0.1,  2. ,  1. ],
       [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
       [ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ]])

plt.figure(1)
plt.imshow(data_1 ,interpolation='gaussian')
plt.colorbar()
