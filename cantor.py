# We're constructing a prototype for the MATLAB implementation
# First, let's write a function to tell us the max iteration of the cantor set that a number belongs in

def maxiteration(n,s):
	i = 0
	mid = l[1]-l[0]/3
	if n >= l[0]+mid and n <= l[1]-mid:
		return i
	else:
		if n >= l[0] and n <= l[0]+mid:
			return (l[0], l[0]+mid)
		elif n >= l[1]-mid and n <= l[1]:
			return (l[1]-mid, l[1])

def maxiteration(n, s):
	i = 0
	while inMid(n,s) == False:
		i += 1
		mid = float(s[1]-s[0]/3)
		if n >= s[0] and n<= s[0] + mid:
			s = (s[0], s[0]+mid)
		if n >= s[0]+mid and n <= s[1]:
			s = (s[0]+mid, s[1])
	return i

def inMid(n, s):
	mid = float(s[1]-s[0])/3
	print "n:  " + str(n)
	print "mid:  " + str(mid)
	print "s[0]:  " + str(s[0])
	print "s[1]:  " + str(s[1])
	print "s[0] + mid:  " + str(s[0]+mid)
	if n >= s[0]+mid and n <= s[1]-mid:
		return True
	else:
		 return False

print inMid(.5, (0, 1))
print inMid(.222222222, (.48592, .78245))
print inMid(.1234, (0,1))
#print maxiteration(.1234, (0,1))
