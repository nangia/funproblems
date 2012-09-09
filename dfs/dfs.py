import itertools
import copy

maxsize = 6

def compatible(permute, cubelist):
	copycubelist = copy.deepcopy(cubelist)
	for index in range(len(permute)):
		copycubelist[index].add(permute[index])
		if len(copycubelist[index]) > maxsize:
			return False
		
	# now check if there are any duplicates
	for i in permute:
		found = False
		for copycubelistelem in copycubelist:
			if i in copycubelistelem:
				if found:
					# we already found this element earlier
					return False
				else:
					found = True
	return True
						
			
def assignmentiterator(cubelist, constraint):
	for permute in itertools.permutations(constraint, 4):
		possiblechild = copy.deepcopy(cubelist)
		for index in range(len(permute)):
			possiblechild[index].add(permute[index])
		if compatible(permute, cubelist):
			yield possiblechild

						
def depthfirstsearch(cubelist, constraintlist):
	if len(constraintlist) == 0:
		print cubelist
	else:
		for assignment in assignmentiterator(cubelist, constraintlist[0]):
			depthfirstsearch(assignment, constraintlist[1:])

def dowork():
	#constraintlist = ["BOXY", "BUCK", "CHAW", "DIGS", "EXAM", "FLIT", "GIRL", "JUMP", "OGRE", "OKAY", "PAWN", "ZEST"]
	#constraintlist = ["BOXY", "BCKU", "ACHW", "DGIS", "AEMX", "FILT", "GILR", "JMPU", "EGOR", "AOKY", "ANPW", "ESTZ"]
	constraintlist = ["ACHW", "AEMX", "ANPW", "AOKY", "BCKU", "BOXY", "DGIS", "EGOR", "ESTZ", "FILT", "GILR", "JMPU" ]
	cubelist = [ set([]), set([]), set([]), set([]) ]
	depthfirstsearch(cubelist, constraintlist)

dowork()
 