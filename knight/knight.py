# knight's tour
import copy
import sys

boardsize = 5

def children(node):
	x = node[0]
	y = node[1]
	combinations = [(1,2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
	for c in combinations:
		x1 = x + c[0]
		y1 = y + c[1]
		if ( (x1 >=0) and (x1 < boardsize) and (y1 >=0) and (y1 < boardsize)):
			yield (x1,y1)
			
			
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