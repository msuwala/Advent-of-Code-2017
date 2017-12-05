import math

# input_ = 39


def plok(input_):
	rc = math.sqrt(input_)
	print(rc)
	rc_ = (rc - 1) / 2
	print(rc_)
	# r = rc//2 + (1 if rc != rc//1 else 0)
	# print(r)

plok(9)
plok(39)
plok(81)
plok(51)