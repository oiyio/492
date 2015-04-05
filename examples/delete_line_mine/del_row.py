wanted = set(['123', '789'])
count=1
with open("lisp_input.txt",'r') as infile, open("list_output.txt",'w') as outfile: 
	for line in infile:
		if(count == 1):
			package_name = line.strip().split(' ')[0]
			outfile.write(package_name)
			outfile.write("\n")
			count=0
		else:
			count=1

				#infile.next()
