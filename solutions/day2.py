def solve_p1():
	with open("../resources/day2") as infile:
		s = 0
		for line in infile:
			line = [int(x) for x in line.split()]
			s += max(line) - min(line)
		print(s)


def solve_p2():
	with open("../resources/day2") as infile:
		s = 0
		for line in infile:
			line = [int(x) for x in line.split()]
			for i in range(len(line)):
				for j in range(i + 1, len(line)):
					if max([line[i], line[j]]) % min([line[i], line[j]]) == 0:
						s += max([line[i], line[j]]) / min([line[i], line[j]])
		print(s)
