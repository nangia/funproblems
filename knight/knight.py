# knight's tour
import copy
import sys

boardsize = 5

# Returns a iterator having all the children (i.e. the notes that can be visited by a knight)
# of a given node
def children(node):
	x = node[0]
	y = node[1]
	# The knight can travel such that its coordinates are incremented/decremented by (1,2) or (2,1)
	combinations = [(1,2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
	for c in combinations:
		x1 = x + c[0]
		y1 = y + c[1]
		# check if after this addition, the coordinates are valid board coordinates
		if ( (x1 >=0) and (x1 < boardsize) and (y1 >=0) and (y1 < boardsize)):
			yield (x1,y1)
			
# This function expects a list of knight positions (a position is a tuple of (x,y) 
# coordinates). Exits when it has found a knight's tour			
def search(toursofar):
	#print depth
	if len(toursofar) == boardsize * boardsize:
		print toursofar
		sys.exit(0)
	else:
		stoursofar = set(toursofar)
		for c in children(toursofar[-1]):
			if not (c in stoursofar):
				thecopy = copy.deepcopy(toursofar)
				thecopy.append(c)
				search(thecopy)
				

search( [ (0,0) ] )
