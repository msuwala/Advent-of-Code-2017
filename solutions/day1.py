test_p1_1 = "1122"
test_p1_2 = "1111"
test_p1_3 = "1234"
test_p1_4 = "91212129"

test_p2_1 = "1212"
test_p2_2 = "1221"
test_p2_3 = "123425"
test_p2_4 = "123123"
test_p2_5 = "12131415"


def solve(input_, delta=1):
	s = 0
	for x in range(len(input_)):
		if input_[x] == input_[(x + delta) % len(input_)]:
			s += int(input_[x])
	print(s)
	return s


# print(solve(test_p1_1) == 3)
# print(solve(test_p1_2) == 4)
# print(solve(test_p1_3) == 0)
# print(solve(test_p1_4) == 9)

# print(solve(test_p2_1, int(len(test_p2_1)/2)) == 6)
# print(solve(test_p2_2, int(len(test_p2_2)/2)) == 0)
# print(solve(test_p2_3, int(len(test_p2_3)/2)) == 4)
# print(solve(test_p2_4, int(len(test_p2_4)/2)) == 12)
# print(solve(test_p2_5, int(len(test_p2_5)/2)) == 4)

with open("../resources/day1") as infile:
	input_ = infile.readline()
	solve(input_, delta=int(len(input_) / 2))
