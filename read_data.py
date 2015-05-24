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


from sys import stdin


class InputData:
    def __init__(self, filenames):
        self.files = filenames
        self.current = -1

    def __next__(self):
        self.current += 1
        if self.current == len(self.files):
            raise StopIteration()
        return read_dat(self.files[self.current])

    def __iter__(self):
        return self


def read_dat(filename, all_same=True):
    "Read data from file and save it to 2d array"
    datar = []
    open_file = filename != "-"
    if open_file:
        try:
            fp = open(filename)
        except Exception:
            return datar
    else:
        fp = stdin
    try:
        for line in fp:
            if line.startswith('#'):
                continue
            datar.append([float(i) for i in line.split()])
    finally:
        if open_file:
            fp.close()
    if all_same and datar:
        l0 = len(datar[0])
        if not all([len(i) == l0 for i in datar]):
            raise IndexError("Not all lines are the same")
    return datar
