# from functools import reduce

# numbers = [
#     input(),
#     input()
# ]
# result = reduce(lambda x, y: x + y, map(lambda i: int(i), numbers))
# print(result)

from posixpath import split


s = input()
numbers = s.split(' ')
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])
if d <= b:
	print(a)
else:
	print(a + c * (d - b))