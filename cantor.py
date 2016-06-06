#The iteration function calculates which iteration a point belongs to in the COMPLEMENT of the Cantor set

#Give us the last iteration of the fractal that n can be found in given the two points S
#Example: citeration(.0001234, (0,1))
def citeration(n, s):
	i = 1
	while inMid(n,s) == False:
		i += 1
		mid = float(s[1]-s[0])/3
		if n >= s[0] and n<= s[0] + mid:
			s = (s[0], s[0]+mid)
		if n >= s[0]+mid and n <= s[1]:
			s = (s[0]+mid, s[1])
	return i

#Is N in the middle third between the points in S?
def inMid(n, s):
	mid = float(s[1]-s[0])/3
	#print "n:  " + str(n)
	#print "mid:  " + str(mid)
	#print "s[0]:  " + str(s[0])
	#print "s[1]:  " + str(s[1])
	#print "s[0] + mid:  " + str(s[0]+mid)
	if n >= s[0]+mid and n <= s[1]-mid:
		return True
	else:
		 return False

