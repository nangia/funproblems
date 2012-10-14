# knight's tour
import copy
import sys

boardsize = 8

children = {}


# Returns a iterator having all the children (i.e. the notes that can be visited by a knight)
# of a given node
def childrenGenerator(node):
	x = node[0]
	y = node[1]
	# The knight can travel such that its coordinates are incremented/decremented by (1,2) or (2,1)
	combinations = [(1,2), (-1, 2), (-1, -2), (1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
	for c in combinations:
		x1 = x + c[0]
		y1 = y + c[1]
		# check if after this addition, the coordinates are valid board coordinates
		if ( (x1 >=0) and (x1 < boardsize) and (y1 >=0) and (y1 < boardsize)):
			yield (x1,y1)
	
# which node has lesser children
def comparisonfunction(n1, n2):
	count1 = children[n1][0]
	count2 = children[n2][0]
	if (count1 < count2):
		return -1
	elif (count1 > count2):
		return 1
	else:
		return 0


def buildChildren():
	for x in xrange(boardsize):
		for y in xrange(boardsize):
			count = 0
			childrenlist = []
			for child in childrenGenerator( (x,y) ):
				childrenlist.append(child)
				count += 1
			children[ (x,y) ] = (count, childrenlist)
	# Now let's sort them also
	for x in xrange(boardsize):
		for y in xrange(boardsize):
			(count, list) = children[ (x,y)]
			sortedlist = sorted(list, comparisonfunction)
			children[ (x,y) ] = (count, sortedlist)


	
		
# This function expects a list of knight positions (a position is a tuple of (x,y) 
# coordinates). Exits when it has found a knight's tour			
def search(toursofar):
	#print "---------------------------------------"
	#print toursofar
	#print depth
	if len(toursofar) == boardsize * boardsize:
		print toursofar
		sys.exit(0)
	else:
		stoursofar = set(toursofar)
		#print toursofar[-1]
		(count, thechildren) = children[toursofar[-1]]
		for c in thechildren:
			if not (c in stoursofar):
				thecopy = copy.deepcopy(toursofar)
				thecopy.append(c)
				search(thecopy)
				


buildChildren()
#print children.values()
search( [ (0,0) ] )
