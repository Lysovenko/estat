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
"Some operations on columns"

import sys
import os
import math


def lin_stat(idata, col_x, col_y):
    ipoints = []
    for data in idata:
        ipoints += data
    N = 0
    X = 0.
    Y = 0.
    X2 = 0.
    XY = 0.
    Y2 = 0.
    for line in ipoints:
        x = line[col_x]
        y = line[col_y]
        N += 1
        X += x
        Y += y
        XY += x * y
        X2 += x ** 2
        Y2 += y ** 2
    D = X2 * N - X ** 2
    a = (XY * N - Y * X) / D
    b = (X2 * Y - XY * X) / D
    if N > 2:
        chi2 = (a ** 2 * X2 + 2 * a * b * X - 2 * a * XY +
                N * b ** 2 - 2 * b * Y + Y2) / (N - 2)
    else:
        chi2 = None
    return [[0, b], [1, a], ['#Chi^2', chi2]]


def poly_fit(idata, col_x, col_y, deg):
    import numpy as np
    ipoints = []
    for data in idata:
        ipoints += data
    arr = np.array(ipoints).transpose()
    res = np.polyfit(arr[col_x], arr[col_y], deg)
    return enumerate(reversed(res))


def chi2(idata, col_x, col_y):
    import numpy as np
    ipoints = []
    for data in idata:
        ipoints += data
    arr = np.array(ipoints).transpose()
    mul = arr[col_x] - arr[col_y]
    mul = mul ** 2
    return mul.sum() / len(mul)
