from cmath import sqrt
from math import ceil
from posixpath import split

def check_x0(x):
	i = 0
	while i < n:
		x = x**2 - nums[i]
		if x < 0:
			return (0)
		i += 1
	return (1)

n = int(input())
s = input()
words = s.split(' ')[:n]
nums = [int(item) for item in words]
nums.sort()
x0 = ceil((sqrt(nums[0])).real)
while check_x0(x0) == 0:
	x0 += 1
print(x0)
