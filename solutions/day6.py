def solve(reg, twist=False):
    seen = dict()
    c = 0
    while seen.get(reg) is None:
        seen.update({reg: c})
        l = list(reg)
        i = l.index(max(l))
        s = l[i]
        l[i] = 0
        while s > 0:
            l[(i + 1) % 16] += 1
            i += 1
            s += -1
        c += 1
        reg = tuple(l)
    return c if not twist else c - seen.get(reg)

with open("../resources/day6") as infile:
    data = tuple(int(x) for x in infile.readline().split())
    print(solve(data))
    print(solve(data, True))
