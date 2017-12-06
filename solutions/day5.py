def part1(infile):
    a = []
    for line in infile:
        a.append(int(line.strip()))
    i = 0
    c = 0
    while 0 <= i < len(a):
        tmp = a[i]
        a[i] += 1
        i += tmp
        c += 1
    return c


def part2(infile):
    a = []
    for line in infile:
        a.append(int(line.strip()))
    i = 0
    c = 0
    while 0 <= i < len(a):
        tmp = a[i]
        a[i] += (-1 if tmp >= 3 else 1)
        i += tmp
        c += 1
    return c

with open("../resources/day5") as infile:
    print(part1(infile))
    infile.seek(0)
    print(part2(infile))
