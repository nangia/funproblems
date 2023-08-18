
import copy
#n queens 

#n x n square 

#partial solution: [col1, col2, col3] i.e. queens are in position (0, Col1) , (1, Col2) ...
# (x, y) = (row, col)


def conflict(row, col, partialsolution):
	if partialsolution == None:
		return False
	for therow, thecol in enumerate(partialsolution):
		if therow == row:
			return True
		if thecol == col:
			return True
		if abs(therow - row) == abs(thecol - col):
			return True
	return False
		

def children(partialsolution, size):
	if partialsolution == None:
		rowtofill = 0
	else:
		rowtofill = len(partialsolution)
	# we are now required to fill rowtofill row (row number starts from 0)
	for i in range(size): 
		# see if ith col can be used 
		if not conflict(rowtofill, i, partialsolution):
			yield i
			
def depthfirst(partialsolution, size, depth):
	#print partialsolution, size, depth 
	if partialsolution != None and (len(partialsolution) == size):
		print(partialsolution)
	else:
		for child in children(partialsolution,size):
			if partialsolution == None:
				depthfirst([child],size, depth + 1)
			else:
				thecopy = copy.deepcopy(partialsolution)
				thecopy.append(child)
				depthfirst(thecopy,size, depth + 1)
			
	
	
def nqueens(size):
	emptylist = [1]
	emptylist.remove(1)
	depthfirst(emptylist, size, 0)
	
nqueens(8)
