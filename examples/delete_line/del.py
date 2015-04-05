wanted = set(['123', '789'])

with open("inputfile.txt",'r') as infile, open("outfile.txt",'w') as outfile: 
    for line in infile:
        if line.startswith('NUM,'):
            UNIT = line.strip().split(',')[1] 
            if UNIT not in wanted:
                for _ in xrange(4):
                    infile.next()
                continue

        outfile.write(line)
