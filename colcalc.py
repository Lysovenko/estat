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
from read_data import read_dat


def expected_value(f, col):
    M = 0.
    I = 0.
    D = 0.
    start = True
    for line in f:
        if line[0] == '#':
            continue
        if start:
            spl = line.split()
            xp = float(spl[0])
            yp = float(spl[col])
            start = False
        else:
            spl = line.split()
            x = float(spl[0])
            y = float(spl[col])
            M += (y * x + yp * xp) * (x - xp) / 2.
            D += (y * x ** 2 + yp * xp ** 2) * (x - xp) / 2.
            I += (y + yp) * (x - xp) / 2.
            xp = x
            yp = y
    print("%g\t%g" % (M/I, D/I - (M/I) ** 2))


def med_ariph(f, col):
    N = 0
    M = 0.
    M2 = 0.
    for line in f:
        if line[0] != '#':
            i = float(line.split()[col])
            N += 1
            M += i
            M2 += i * i
    M_ = M/N
    S2_ = M2 / N - M_ ** 2
    S_ = math.sqrt(S2_)
    print(M_, S2_, S_, N, '|', M, M2)


def lin_stat(fnames, col):
    ipoints = []
    for fname in fnames:
        ipoints += read_dat(fname)
    N = 0
    X = 0.
    Y = 0.
    X2 = 0.
    XY = 0.
    for line in ipoints:
        x = line[0]
        y = line[col]
        N += 1
        X += x
        Y += y
        XY += x * y
        X2 += x ** 2
    D = X2 * N - X ** 2
    a = (XY * N - Y * X) / D
    b = (X2 * Y - XY * X) / D
    return [[0, b], [1, a]]
