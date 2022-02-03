from posixpath import split

def get_square_count(a, b, acc):
	min = a
	max = b
	if a > b:
		min = b
		max = a
	count = max // min
	tail = max % min
	if tail == 0:
		return count + acc
	else:
		return get_square_count(min, tail, acc + count)

s = input()
numbers = s.split(' ')
n = int(numbers[0])
m = int(numbers[1])
i = get_square_count(m, n, 0)
print(i)
