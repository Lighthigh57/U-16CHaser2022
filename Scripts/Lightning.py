import random
import Command

#PlayerName = Light

priority = []
"""priority = 優先度"""

run = None
"""instance of Command class"""

last = 0
"""last direction"""

side = 0
"""My Cliant's side"""

map = None
"""Map on firld"""

Check_Zone = 0
"""Interval of Map_Check"""

Safety_Heart = 0
"""ModeChange border"""

item = 0

def main():
	global run
	global priority

	turn = 0
	last = 0
	while True:
		priority = [0 for i in range(9)]
		last = Checker(last, run.get_ready(), turn)
		turn += 1
"""
def map_Check(map):
	マップを調べて取り残さない
	CUTX = 5
	CUTY = 5

	result = [[0 for i in range(int(len(map[0])/CUTX))] for j in range(int(len(map)/CUTY))]

	for y in range(len(result)):
		temp = map[y*CUTY:y*CUTY+CUTY]
		for x in range(len(result[0])):
			check = []
			for i in temp:
				check += i[x*CUTX:x*CUTX+CUTX]
			for j in check:
				if j == 9:
					result[y][x] += 1
	
	ave = 0  
	for a in result:
		for b in a:
			ave += b
	ave /= 9
	nice =[]
	for y_in,y in enumerate(result):
		for x_in,x in enumerate(y):
			if x > ave:
				nice += [y_in*3+x_in]
	print(nice)
"""
	
def solve_diagonal(target, com):
	"""斜めに物が見えた時の処理"""
	global priority
	if target < 3:  # Where this is for X
		y = 1
	else:
		y = 7
	if target == 0 or target == 6:  # Where this is for X
		x = 3
	else:
		x = 5
	if com == "avoid":  # if this is enemy
		priority[x] = -1
		priority[y] = -1
	else:  # if this is item
		priority[x] += 1
		priority[y] += 1

def Checker(last, ready_Value, turn) -> int:
	"""
	敵いたら潰します(笑)
	"""
	global run
	global priority
	global item

	for i in range(0, 9):  # Safe Command
		if ready_Value[i] == 3:  # Can I get now?
			if i % 2 == 1:
				priority[i] += 1
			else:
				solve_diagonal(i, "get")
	# Danger Command
	for i in range(0, 9):
		if ready_Value[i] == 1:  # Can I put there now?
			if i % 2 == 0:
				solve_diagonal(i, "avoid")
			else:
				run.move("put", i)
				break
		if ready_Value[i] == 2:  # There is a block?
			priority[i] = -2

	max = priority[1]  # maximum value
	nowmax = [1]  # direction index who it has maximum

	# find maximum value in priority list(look like search sort)
	for i in range(3, 8, 2):
		if max < priority[i]:
			max = priority[i]
			nowmax = [i]
		elif max == priority[i]:
			nowmax += [i]

	if len(nowmax) != 1:  # remove last place
		if ((last == 1) and (7 in nowmax)):
			nowmax.remove(7)
		elif ((last == 3) and (5 in nowmax)):
			nowmax.remove(5)
		elif ((last == 5) and (3 in nowmax)):
			nowmax.remove(3)
		elif ((last == 7) and (1 in nowmax)):
			nowmax.remove(1)
	if max < 0:  # I should go to Danger Zone!!!
		run.move("look", 1)
		return 0
	else:
		goto = nowmax[random.randint(0,len(nowmax)-1)]
		run.move("walk", goto)
	return goto

if __name__ == "__main__":
	Side = int(input("Cool:0,Hot:1 : "))
	run = Command.Command()  # Set Command instance
	main()
