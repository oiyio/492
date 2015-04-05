# not working

# pkgname in cache

#Check whether a package with the name given by pkgname exists in the cache for the native architecture. If pkgname includes a colon, the part after the colon is used as the architecture.
#https://apt.alioth.debian.org/python-apt-doc/library/apt_pkg.html

# apt_pkg.Package class ve apt.package.Package class'i arasindaki fark nedir?
# apt.cache.Cache class ve apt_pkg_Cache class'i arasindaki fark nedir?

import apt_pkg
import apt.cache

def main():
    """Main."""
    apt_pkg.init_config()
    apt_pkg.init_system()
    cache1 = apt_pkg.Cache()
    cache2 = apt.cache.Cache()
    cache2.update()
    print "Essential packages:"
    for pkg in cache1.packages:
        if pkg.essential:
            print " ", pkg.name

    for pkg in cache1.packages:
        if cache2[pkg.name].is_installed:
            print " ", pkg.name

    print "Important packages:"
    for pkg in cache1.packages:
        if pkg.important:
            print " ", pkg.name

if __name__ == "__main__":
    main()
