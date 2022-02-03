from posixpath import split

def func(i, acc):
	if i == 0:
		return acc
	i = i - a[i - 1]
	if i == 0:
		return acc + 1
	return func(i + b[i - 1], acc + 1)
	

n = int(input())
s1 = input()
s2 = input()
words1 = s1.split(' ')[:n]
words2 = s2.split(' ')[:n]
a = [int(item) for item in words1]
b = [int(item) for item in words2]
print(func(n, 0))