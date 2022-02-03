from posixpath import split

def check_way(x, y):
	if x == n and y == m:
		return 1
	if x > n or y > m:
		return 0
	return check_way(x + 2, y + 1) + check_way(x + 1, y + 2)

s = input()
numbers = s.split(' ')
n = int(numbers[0])
m = int(numbers[1])
# min = n
# max = m
# if n > m:
# 	min = m
# 	max = n
# if ((m + n - 5) % 3 != 0) or (2 * min < max):
# 	print("0")
# else:
print(check_way(1, 1))
