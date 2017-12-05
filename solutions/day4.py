def part1(infile):
	s = 0
	for line in infile:
		if len(line.split()) == len(set(line.split())):
			s += 1
	return s


def part2(infile):
	s = 0
	for line in infile:
		t = [''.join(sorted(x)) for x in line.split()]
		if len(set(t)) == len(t):
			s += 1
	return s


with open("../resources/day4") as infile:
	print("Part one answer: ", part1(infile))
	infile.seek(0)
	print("Part two answer: ", part2(infile))
