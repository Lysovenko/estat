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


from sys import stdin, stderr


class InputData:
    def __init__(self, filenames, split):
        self.filenames = filenames
        self.cur_name = -1
        self.previous = 0
        self.split = split

    def __next__(self):
        data = []
        while not data:
            if not self.split or self.previous == 0:
                self.cur_name += 1
                if self.cur_name == len(self.filenames):
                    raise StopIteration()
            data = self.read_dat(self.filenames[self.cur_name])
        return data

    def __iter__(self):
        return self

    def read_dat(self, filename, all_same=True):
        "Read data from file and save it to 2d array"
        datar = []
        open_file = filename != "-"
        if open_file:
            try:
                fp = open(filename)
            except IOError as err:
                stderr.write("Can't open %s: %s\n" % (filename, err.strerror))
                return datar
        else:
            fp = stdin
        try:
            datar = self.read_lines(fp)
        finally:
            if open_file:
                fp.close()
        if all_same and datar:
            l0 = len(datar[0])
            if not all([len(i) == l0 for i in datar]):
                raise IndexError("Not all lines are the same")
        return datar

    def read_lines(self, fp):
        datar = []
        empty = 0
        set_end = 0
        if self.split and fp.seekable():
            fp.seek(self.previous)
        for line in iter(fp.readline, ""):
            if line.startswith("#"):
                continue
            if line.isspace():
                empty += 1
                if self.split and empty >= 2:
                    if fp.seekable():
                        set_end = fp.tell()
                        break
                continue
            else:
                empty = 0
            datar.append([float(i) for i in line.split()])
        self.previous = set_end
        return datar
