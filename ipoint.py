#!/usr/bin/env python3
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
"Input point"

from sys import stdout


def parse_options():
    from optparse import OptionParser
    parser = OptionParser(usage="%prog [OPTIONS] <FILENAME(S)>",
                          version="%prog 0.1")
    parser.disable_interspersed_args()
    parser.add_option(
        "-o", "--out", dest="ofilename",
        help="write result to to FILE", metavar="FILE", default=None)
    parser.add_option(
        "-a", "--average", dest="average",
        action="store_true", default=False, help="calculate average")
    parser.add_option(
        "-d", "--dispersion", dest="dispersion",
        action="store_true", default=False, help="calculate dispersion")
    return parser.parse_args()


def run():
    options, in_names = parse_options()
    if not in_names:
        raise ValueError('no input names')
    result = None
    if options.average:
        from calc1d import calc_med_ariph
        result = calc_med_ariph(in_names)
    if options.dispersion:
        from calc1d import calc_dispersion
        result = calc_dispersion(in_names)
    if options.ofilename:
        ouf = open(options.ofilename, "w")
    else:
        from sys import stdout
        ouf = stdout
    with ouf:
        for i in result:
            ouf.write('\t'.join([str(j) for j in i]) + '\n')


# if __name__ == "__main__":
#     options, in_names = parse_options()
#     larr = []
#     for name in in_names:
#         with open(name) as f:
#             lines = f.readlines()
#             if options.rm_com:
#                 lines = [i for i in lines if not i.startswith('#')]
#             larr.append(lines)
#     if len(larr) < 2:
#         exit(1)
#     lmax = max([len(i) for i in larr])
#     allsame = all([len(i) == lmax for i in larr])
#     if not allsame:
#         exit(2)
#     if options.ofilename:
#         ouf = open(options.ofilename, "w")
#     else:
#         from sys import stdout
#         ouf = stdout
#     with ouf:
#         for i in range(lmax):
#             ouf.write('\t'.join([j[i].strip() for j in larr]))
#             ouf.write('\n')
