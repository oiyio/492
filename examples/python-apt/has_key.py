import apt

foo = apt.cache.Cache()

print (foo.has_key('ia32-libs-multiarch'))

print(foo.has_key('ia32-libs-multiarch:i386'))

print(foo.has_key('skype'))

print(foo.has_key('skype:i386'))
