if __name__ == "__main__":
    from sys import argv
    from math import floor
    fname = argv[1]
    nms = tuple(map(lambda x: x.split(), argv[2].split(',')))
    begin = float(argv[3])
    end = float(argv[4])
    points = int(argv[5])
    step = (end - begin) / (points - 1)
    nats = sum(map(lambda x: int(x[0]), nms))
    boof = [0.0 for i in range(points)]
    with open(fname) as fp:
        for nm in nms:
            n = int(nm[0])
            m = float(nm[1]) / 2
            for i in range(n):
                e = sum(map(lambda x: float(x)**2, fp.readline().split())) * m
                fbp = floor((e - begin) / step)
                sseg = (e - (begin + step * fbp)) / step
                try:
                    boof[fbp] += (1. - sseg) / nats
                    boof[fbp+1] += sseg / nats
                except IndexError:
                    pass
    for i, p in enumerate(boof):
        print(f"{i*step+begin}\t{p}")
