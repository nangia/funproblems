
from collections import deque

grid01 = [
"003020600",
"900305001",
"001806400",
"008102900",
"700000008",
"006708200",
"002609500",
"800203009",
"005010300",
]


grid02 = [
"000700800",
"006000031",
"040002000",
"024070000",
"010030080",
"000060290",
"000800070",
"860000500",
"002006000"
]

def location2cube(row,col):
	cuberow = row / 3
	cuberowrem = row % 3
	
	cubecol = col / 3
	cubecolrem = col % 3
	return ( cuberow, cuberowrem, cubecol, cubecolrem )

def cube2location(cuberow, cuberowrem, cubecol, cubecolrem):
	return (cuberow * 3 + cuberowrem, cubecol * 3 + cubecolrem)

def getGrid(list):
	result = [[], [], [], [], [], [], [], [], []]
	num = 0
	for str in list:
		for s in str:
			if (s == "0") or (s =="."):
				result[num].append(set([1,2,3,4,5,6,7,8,9]))
			else:
				result[num].append(set([int(s)]))
		num += 1
	return result

	
# def grid ===> deque of (row, col) where there is only one number (i.e. set size is 1)
def grid2constraint(grid):
	constraintdeque = deque([])
	for row in xrange(0,9):
		for col in xrange(0, 9):
			if (len(grid[row][col]) == 1):
				constraintdeque.append([row,col])
	return constraintdeque
				

def positionsaffected(grid, location):
	row = location[0]
	col = location [1]
	assert( len(grid[row][col]) == 1)
	
	# let's first look at cols which get affected
	for c in xrange(0,9):
		if (c != col):
			yield (row, c)
	# let's first look at rows which get affected
	for r in xrange(0,9):
		if (r != row):
			yield (r, col)
	# let's look at the cube location which get affected
	cuberow, cuberowrem, cubecol, cubecolrem = location2cube(row, col)
	for r in xrange(0, 3):
		for c in xrange(0, 3):
			if not((r == cuberowrem) or (c == cubecolrem)):
				yield cube2location(cuberow, r, cubecol, c)
				
	

	
			
def printallseq(seq):
	for s in seq:
		print s


		
def printgrid(grid):
	pass

def gridconstraintresolve(grid):
	constraintdeque = grid2constraint(grid) # deque
	#print constraintdeque
	while ( len(constraintdeque) != 0):
		first = constraintdeque.popleft()
		#print "first =", first
		for affectedpos in positionsaffected(grid, first):
			#print "affectedpos =", affectedpos
			element = 0
			for x in grid[first[0]][first[1]]:
				element = x
			#print "element = ", element
			r = affectedpos[0]
			c = affectedpos[1]
			#print (r,c)
			#print grid[r][c]
			if element in grid[r][c]:
				(grid[r][c]).remove(element)
				#print grid[r][c]
				if len(grid[r][c]) == 1:
					constraintdeque.append((r,c))
				if len(grid[r][c]) == 0:
					print "Invalid"
					return []
			#print "-----------------------------------------------"
		#print "======================================"
		#break
	return grid
				
				
				
grid03 = [
[set([1]), set([3]), set([5]), set([7]), set([1, 4, 5, 9]), set([1, 3, 4, 5, 9]), set([8]), set([2, 4, 5, 6]), set([2, 4, 5, 6, 9])] , 

[set([2]), set([5, 7, 8, 9]), set([6]), set([4, 5, 9]), set([4, 5, 8,  9]), set([4, 5, 8, 9]), set([4, 7, 9]), set([3]), set([1])], 

[set([1, 3, 5, 7, 9]), set([4]), set([1, 3, 5, 7, 8, 9]), set([1, 3, 5, 6, 9]), set([1, 5, 8, 9]),
 set([2]), set([6, 7, 9]), set([5, 6]), set([5, 6, 7, 9])], 
 
[set([3, 5, 6, 9]), set([2]), set([4]), set([1]), set([7]), set([1, 5, 8, 9]), set([1, 3, 6]),  set([1, 5, 6]), set([3, 5, 6])], 

[set([5, 6, 7, 9]), set([1]), set([5, 7, 9]), set([2, 4, 5, 9]), set([3]), set([4, 5, 9]), set([4, 6, 7]), set([8]), set([4, 5 , 6, 7])], 

[set([3, 5, 7]), set([3, 5, 7, 8]), set([3, 5, 7, 8]), set([1, 4, 5]) , set([6]), set([1, 4, 5, 8]), set([2]), set([9]), set([3, 4, 5, 7])], 

[set([1, 3, 4, 5, 9]), set([3, 5, 9]), set([1, 3, 5, 9]), set([8]), set([1]),  set([1, 3, 4, 5, 9]), set([1, 3, 4, 6, 9]), set([7]), set([2, 3, 4, 6, 9])],

[set([8]), set([6]), set([1, 3, 7, 9]), set([1, 2, 3, 4, 9]), set([1, 2, 4, 9]), set([1, 3, 4, 7, 9]), set([5]), set([1, 2, 4]), set([2, 3, 4, 9])], 

[set([1, 3, 4 , 5, 7, 9]), set([3, 5, 7, 9]), set([2]), set([1, 3, 4, 5, 9]), set([1, 4, 5, 9] ), set([6]), set([1, 3, 4, 9]), set([4]), set([3, 4, 8, 9])]]
 
#print grid03
#thegrid = getGrid(grid03)
print gridconstraintresolve(grid03)



	