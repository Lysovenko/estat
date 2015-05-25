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
from read_data import InputData


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
    parser.add_option(
        "-c", "--column", type=int, help="selected column", default=1)
    parser.add_option(
        "--lin-reg", action="store_true", default=False,
        dest="lin_regr", help="linear regresion")
    parser.add_option(
        "--polinomial", default=None, dest="polinomial",
        help="Polinomial fit", type=int)
    parser.add_option(
        "--caver", action="store_true", default=False,
        dest="col_aver", help="column average")
    return parser.parse_args()


def run():
    options, in_names = parse_options()
    if not in_names:
        raise ValueError("It is no input names")
    idata = InputData(in_names)
    result = None
    if options.average:
        from calc1d import calc_med_ariph
        result = calc_med_ariph(idata)
    if options.dispersion:
        from calc1d import calc_dispersion
        result = calc_dispersion(idata)
    if options.lin_regr:
        from colcalc import lin_stat
        result = lin_stat(idata, options.column - 1)
    if options.polinomial:
        from colcalc import poly_fit
        result = poly_fit(idata, options.column - 1, options.polinomial)
    if options.ofilename:
        ouf = open(options.ofilename, "w")
    else:
        from sys import stdout
        ouf = stdout
    with ouf:
        for i in result:
            ouf.write('\t'.join([str(j) for j in i]) + '\n')


if __name__ == '__main__':
    print(parse_options())
