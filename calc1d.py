# Copyright 2015 Serhiy Lysovenko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"Calculate sungledimentional statistics"


import numpy as np


def calc_med_ariph(idata):
    shape = None
    result = None
    ntored = 0
    for data in idata:
        dat = np.array(data)
        if shape is None:
            shape = dat.shape
            result = dat
            nstored = 1
            continue
        elif shape != dat.shape:
            raise ValueError('Shapes are not the same')
        nstored += 1
        result += (dat - result) / nstored
    return result


def calc_dispersion(idata):
    shape = None
    result1 = None
    result2 = None
    ntored = 0
    for data in idata:
        dat = np.array(data)
        if shape is None:
            shape = dat.shape
            result1 = dat ** 2
            result2 = dat
            nstored = 1
            continue
        elif shape != dat.shape:
            raise ValueError('Shapes are not the same')
        nstored += 1
        result1 += (dat ** 2 - result1) / nstored
        result2 += (dat - result2) / nstored
    return result1 - result2 ** 2
