import apt
cache = apt.Cache()
Games = [pkg for pkg in cache if pkg.section.endswith("/lisp")]
print("\n".join(map(lambda x: x.name, Games[1:10])))
