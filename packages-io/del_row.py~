import apt
import os
import sys

def del_lines():
	count=1
	with open("input/lisp_input.txt",'r') as infile, open("output/lisp_output.txt",'w') as outfile: 
		for line in infile:
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


					#infile.next()

cache = apt.cache.Cache()
print "before update"
cache.update()   # error is in this line
print "after update"

del_lines()
print ("done")
