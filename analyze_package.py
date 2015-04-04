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
	
	print "description :  "+ vrs[0].description
	print "summary : " + vrs[0].summary
	print "uri : " + vrs[0].uri
	print "source_name : " + vrs[0].source_name
	print "section : " + vrs[0].section
	print "homepage : " + vrs[0].homepage
	print ["dependencies : "] + vrs[0].dependencies
	print "\n"
	print "\n"
	print "\n"


cache = apt.cache.Cache()
print "before update"
cache.update()   # error is in this line
print "after update"

installPackage(cache,"stellarium")
installPackage(cache,"kstars")
installPackage(cache,"r-cran-genetics")
installPackage(cache,"r-cran-gdata")
installPackage(cache,"r-cran-mgcv")
installPackage(cache,"r-cran-qtl")
installPackage(cache,"r-cran-gmaps")
installPackage(cache,"r-other-rot")

print "others : "
	
installPackage(cache,"abinit")
installPackage(cache,"abyss")
installPackage(cache,"autogrid")
installPackage(cache,"autogrid-test")
installPackage(cache,"avogadro-data")
installPackage(cache,"c2hs")
installPackage(cache,"cabal-install")
