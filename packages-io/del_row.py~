import apt
import os
import sys


for i in os.listdir("input/"):
	if i.endswith(".txt"):
		print i

def del_lines():
	for i in os.listdir("input/"):
		if i.endswith(".txt"):
			with open(("input/"+i),'r') as infile, open(("output/"+i),'w') as outfile:
				count=1
				for line in infile:
					if(count == 1): # first line of each two lines
						package_name = line.strip().split(' ')[0]
						outfile.write(package_name)
						outfile.write(" ")
						try:
							pkg = cache[package_name]
						except Exception, arg:
							pass
							#print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))
						vrs = pkg.versions
						outfile.write(vrs[0].version)
						outfile.write("\n")
						count = 0
					else:
						count = 1


						#infile.next()

cache = apt.cache.Cache()
print "before update"
cache.update()   # error is in this line
print "after update"

del_lines()
print ("done")
