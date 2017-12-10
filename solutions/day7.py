import re

# from part 1 solved in browser using "find"
root = "gynfwly"


def solve():
	with open("../resources/day7") as infile:
		tree = dict()
		for line in infile:
			match = re.match(r"^([a-z]*)\s\(([0-9]*)\)(\s->\s)?(.*)", line)
			tree.update({match.group(1): (int(match.group(2)), match.group(4).split(", "))})
	step(tree, root)


def step(tree: dict, node: str):
	children = tree.get(node)[1]
	if children == [''] or :



def weight(tree: dict, node: str):
	children = tree.get(node)[1]
	if children == ['']:
		return tree.get(node)[0]
	else:
		s = 0
		for child in children:
			s += weight(tree, child)
		return tree.get(node)[0] + s

if __name__ == "__main__":
	solve()
