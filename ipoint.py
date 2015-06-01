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
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Calculates experimental statistics.")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1")
    parser.add_argument(
        "-o", "--out", dest="ofilename",
        help="write result to to FILE", metavar="FILE", default=None)
    parser.add_argument(
        "-a", "--average", dest="average",
        action="store_true", default=False, help="calculate average")
    parser.add_argument(
        "-d", "--dispersion", dest="dispersion",
        action="store_true", default=False, help="calculate dispersion")
    parser.add_argument(
        "-c", "--column-y", type=int, help="column with y values", default=2,
        dest="col_y")
    parser.add_argument(
        "--column-x", type=int, help="column with x values", default=1,
        dest="col_x")
    parser.add_argument(
        "--lin-reg", action="store_true", default=False,
        dest="lin_regr", help="linear regresion")
    parser.add_argument(
        "--polinomial", default=None, dest="polinomial",
        help="Polinomial fit", type=int, metavar="degree")
    parser.add_argument(
        "--caver", action="store_true", default=False,
        dest="col_aver", help="column average")
    parser.add_argument("files", metavar="File", type=str, nargs="+",
                        help="Files to process")
    return parser.parse_args()


def run():
    args = parse_options()
    idata = InputData(args.files)
    result = None
    if args.average:
        from calc1d import calc_med_ariph
        result = calc_med_ariph(idata)
    if args.dispersion:
        from calc1d import calc_dispersion
        result = calc_dispersion(idata, args.col_x - 1)
    if args.lin_regr:
        from colcalc import lin_stat
        result = lin_stat(idata, args.col_x - 1, args.col_y - 1)
    if args.polinomial:
        from colcalc import poly_fit
        result = poly_fit(
            idata, args.col_x - 1, args.col_y - 1, args.polinomial)
    if args.ofilename:
        ouf = open(args.ofilename, "w")
    else:
        from sys import stdout
        ouf = stdout
    with ouf:
        for i in result:
            ouf.write("\t".join(map(str, i)) + "\n")


if __name__ == "__main__":
    print(parse_options())
