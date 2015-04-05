import apt
import os
def installPackage(cache,pkg_name):

        

        pkg = cache[pkg_name]
	print ["id of the package : "] + [pkg.id]
        print ["is_installed : "] + [pkg.is_installed]
        print "section : " + pkg.section
	print "shortname : " + pkg.shortname
	print "name : " + pkg.name 

	vrs = pkg.versions
	
	print "summary : " + vrs[0].summary
	print "uri : " + vrs[0].uri
	print "source_name : " + vrs[0].source_name
	print "section : " + vrs[0].section
	print "version : " + vrs[0].version


	print "\n"



cache = apt.cache.Cache()
print "before update"
cache.update()   # error is in this line
print "after update"

installPackage(cache,"anthy-el")
installPackage(cache,"anything-el")
installPackage(cache,"aplus-fsf-el")
