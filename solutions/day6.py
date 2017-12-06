def solve(infile, twist=False):
    reg = []
    seen = []
    for x in infile.readline().split():
        reg.append(int(x))
    c = 0
    while seen.count(','.join(map(str, reg))) == 0:
        seen.append(','.join(map(str, reg)))
        i = reg.index(max(reg))
        s = reg[i]
        reg[i] = 0
        while s > 0:
            reg[(i + 1) % len(reg)] += 1
            i += 1
            s += -1
        c += 1
    return c if not twist else c - seen.index(','.join(map(str, reg)))

with open("../resources/day6") as infile:
    print(solve(infile))
    infile.seek(0)
    print(solve(infile, True))
