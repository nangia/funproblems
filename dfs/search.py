


#getconstraint (string) ===> should returns set of constraints
def getconstraint(thestring):
	constraintlist = set([])
	length = len(thestring)
	for i in range(length):
		for j in range(i + 1, length):
			if thestring[i] < thestring[j]:
				constraintlist.add( (thestring[i], thestring[j]) )
			else:
				constraintlist.add( (thestring[j], thestring[i]) )
	return constraintlist
			
def getuniversal(stringlist):
	concatenated = ""
	for s in stringlist:
		concatenated += s
	return getconstraint(concatenated)
	#universallist = []
	#for s in stringlist:
	#	clist = getconstraint(s)
	#	for x in clist:
	#		universallist.append(x)
	#		
	#return universallist
#getuniversal(string) ===> should return universal graph


#compute union of all sets of constraints
#subtraction of sets (U - (union of all sets of constraints))

def dowork():
	constraintlist = ["BOXY", "BUCK", "CHAW", "DIGS", "EXAM", "FLIT", "GIRL", "JUMP", "OGRE", "OKAY", "PAWN", "ZEST"]
	universal = getuniversal(constraintlist)
	allconstraints = set([])
	for s in constraintlist:
		allconstraints = allconstraints.union(getconstraint(s))
	difference = universal - allconstraints
	allbase = "ABCDEFGHIJKLMNOPRSTUWXYZ";
	allsets = { 'A': set([]) }
	for x in allbase:
		allsets[x] = set([])
	for d in difference:
		allsets[d[0]].add(d[1])
	print allsets
