import apt

fo = open("foo.txt", "wb")

cache = apt.Cache()
Games = [pkg for pkg in cache if pkg.section.endswith("/lisp")]
for i in range(len(Games)):
	print Games[i].name


# Close opend file
fo.close()


