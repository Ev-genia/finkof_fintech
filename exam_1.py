from posixpath import split

s = input()
numbers = s.split(' ')
a = int(numbers[0])
b = int(numbers[1])
n = int(numbers[2])
if n == 0:
	if a == b:
		print("YES")
	else:
		print("NO")
elif a == 0:
	print("NO")
elif a <= b:
	print("NO")
elif (a - b) % 2 != 0:
	print("NO")
elif (a - b) < 2 * n:
	print("NO")
else:
	print("YES")