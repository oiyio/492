from subprocess import call
from os import system

# "key" variable holds the keyword which the user typed to search for.

def call_sh(key):
	##call("./cache_search.sh " + key, shell=True)
	# Execute the command (a string) in a subshell.
	# cache_search.sh shell script dosyasi subshell calistirilacak.
	system("./cache_search.sh " + key) 

def parse_file(key):
	f_cache = open("cache_list.txt", "r+")
	f_names = open("name_list.txt", "r+")
	f_other = open("other_list.txt", "r+")
	for line in f_cache:  #f_cache dosyasi, apt-cache search pkgname sonuclarini tutuyordu.
				#Bu dosyadaki herbir satir alinir her for dongusunde.
		sLine = line.split()  
		#split :satirdaki tum kelimeleri element olarak iceren bir list return eder.
		#sLine bu list'i tutar.
		print "line : " + line;
		if key.lower() in sLine[0].lower(): 
		#bu satirin icerdigi kelimelere arasinda, bizim search etmek istedigimiz "key" variable var mi

			#evet var.
			if check_primary(key.lower(), sLine[0].lower()):
			
					f_names.write(sLine[0]+"\n")
			else:
					f_other.write(sLine[0]+"\n")
	f_cache.close()
	f_names.close()
	f_other.close()

def check_primary(first, second):
	for i in range(len(first)):
		if first[i] != second[i]:
			return False
	return True
