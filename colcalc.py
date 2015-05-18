#!/usr/bin/python
# -*- coding: utf8
# Some operations on columns
import sys
import os
import math


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


def lin_stat(f, col):
    N = 0
    X = 0.
    Y = 0.
    X2 = 0.
    XY = 0.
    for line in f:
        if line[0] == '#':
            continue
        spl = line.split()
        x = float(spl[0])
        y = float(spl[col])
        N += 1
        X += x
        Y += y
        XY += x * y
        X2 += x ** 2
    D = X2 * N - X ** 2
    a = (XY * N - Y * X) / D
    b = (X2 * Y - XY * X) / D
    print "%g *x + %g" % (a, b)
if len(sys.argv) < 2:
    print "usage: colcalc <file> <column> [opts]"
    sys.exit()
if sys.argv[1] == '-':
    f = sys.stdin
else:
    f = open(sys.argv[1])
col = int(sys.argv[2])
if len(sys.argv) == 3 or '-exp_val' in sys.argv:
    expected_value(f, col)
elif '-average' in sys.argv:
    med_ariph(f, col)
elif '-lin-stat' in sys.argv:
    lin_stat(f, col)
if sys.argv[1] != '-':
    f.close()
