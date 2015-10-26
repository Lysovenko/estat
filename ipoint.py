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
    parser.add_argument(
        "-m", "--mode", dest="mode", type=str, required=True, metavar="Mode",
        choices={"aver", "average", "disp", "dispersion", "lr",
                 "linear-regresion", "pol", "polinomial", "caver",
                 "column-average", "chi2"}, help="Calculation mode")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1")
    parser.add_argument(
        "-o", "--out", dest="ofilename",
        help="write result to to FILE", metavar="FILE", default=None)
    parser.add_argument(
        "-d", "--degree", dest="degree", type=int, default=2,
        help="degree of polinomial")
    parser.add_argument(
        "-c", "--column-y", type=int, help="column with y values", default=2,
        dest="col_y")
    parser.add_argument(
        "--column-x", type=int, help="column with x values", default=1,
        dest="col_x")
    parser.add_argument(
        "-s", "--split", dest="split", action="store_true", default=False,
        help="split single file")
    parser.add_argument("files", metavar="File", type=str, nargs="+",
                        help="Files to process")
    return parser.parse_args()


def run():
    args = parse_options()
    idata = InputData(args.files, args.split)
    result = None
    if args.mode in {"aver", "average"}:
        from calc1d import calc_med_ariph
        result = calc_med_ariph(idata)
    elif args.mode in {"disp", "dispersion"}:
        from calc1d import calc_dispersion
        result = calc_dispersion(idata, args.col_x - 1)
    elif args.mode in {"lr", "linear-regresion"}:
        from colcalc import lin_stat
        result = lin_stat(idata, args.col_x - 1, args.col_y - 1)
    elif args.mode in {"pol", "polinomial"}:
        from colcalc import poly_fit
        result = poly_fit(
            idata, args.col_x - 1, args.col_y - 1, args.degree)
    elif args.mode == "chi2":
        from colcalc import chi2
        result = [[chi2(idata, args.col_x - 1, args.col_y - 1)]]
    if args.ofilename:
        ouf = open(args.ofilename, "w")
    else:
        ouf = stdout
    with ouf:
        for i in result:
            ouf.write("\t".join(map(str, i)) + "\n")
