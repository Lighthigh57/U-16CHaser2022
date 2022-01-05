import random

test = [[random.randint(0,1) for i in range(15)] for j in range(15)]
CUTX = 5
CUTY = 5

result = [[0 for i in range(int(15/CUTX))] for j in range(int(15/CUTY))]

for y in range(len(result)):
	temp = test[y*CUTY:y*CUTY+CUTY]
	for x in range(len(result[0])):
		check = []
		for i in temp:
			check += i[x*CUTX:x*CUTX+CUTX]
		print(str(y)+" "+str(x))
		for j in check:
			if j == 1:
				result[y][x] += 1

print(result)
