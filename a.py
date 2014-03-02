from math import *

def readinto(f, numsats, numstorms):
	satellitelist = []
	stormlist = []

	for i in range(numsats):
		newline = f.readline().split()
		satellitelist.append((float(newline[0]), float(newline[1]), float(newline[2])))
	for i in range(numstorms):
		newline = f.readline().split()
		stormlist.append((float(newline[0]), float(newline[1]), float(newline[2])))
	return satellitelist, stormlist

def func(satl, storml):
	r = 20000/3.14159265358979323
	rmlist = []
	num = 0
	if satl == [] or storml == [] or satl is None or storml is None:
		return 0
	#print satl
	x, y, z = satl[0]
	for a, b, c in storml:
		if (x-a)*(x-a) + (y-b)*(y-b) + (z-c)*(z-c) <= x*x + y*y + z*z - r*r:
			rmlist.append((a,b,c)) #must be tuples when read in
		#print "Printing rmlist"
		#print rmlist
	for item in rmlist:
		#print item
		storml.remove(item)
	num = len(rmlist)
	rmlist = []
	whocares = satl.pop(0)
	#print satl
	#print newsatlist
	return num + func(satl, storml)

with open("a.in", 'r') as f:
	line = f.readline().split()
	while True:
		if len(line) == 2 and int(line[0]) == 0 and int(line[1]) == 0:
			break
		satlist, stormlist = readinto(f, int(line[0]), int(line[1]))
		#print(satlist)
		#print(stormlist)
		print func(satlist, stormlist)
		line = f.readline().split()
