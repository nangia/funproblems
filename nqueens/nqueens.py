
import copy
import argparse

# n queens problem solution for n x n square chess board.

#partial solution: [col1, col2, col3] i.e. queens are in position (0, Col1) , (1, Col2) ...
# (x, y) = (row, col)


# If we add another queen at position (row,col) will it conflict with the partialsolution?
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
		

# yield the children of a particular board position
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
			
# recursive depth first solution to search for n-queens problem
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
	emptylist = []
	depthfirst(emptylist, size, 0)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Print solution to the nqueens problem')
	parser.add_argument('boardsize', type=int, help='size of the board')
	args = parser.parse_args()
	if args.boardsize > 0:
		nqueens(args.boardsize)


