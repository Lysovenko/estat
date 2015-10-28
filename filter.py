#/usr/bin/env python3
#not implemented file
from sys import argv
in_file = open(argv[1])
not_more = float(argv[2])
result = []
prev = None
for line in in_file:
    if line.startswith('#') or line.isspace():
        continue
    if prev is not None:
        if float(line.split()[1]) > not_more + prev:
            result.append('#' + line)
        else:
            result.append(line)
            prev = float(line.split()[1])
    else:
        if not line.startswith('#') and not line.isspace():
            prev = float(line.split()[1])
in_file.close()
out = open(argv[1], 'w')
for i in result:
    out.write(i)
