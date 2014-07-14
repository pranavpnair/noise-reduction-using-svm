#write positive labels first and then negative labels

import sys
s=str(sys.argv[1])
f=open(sys.argv[2])
g=open(sys.argv[3],'w')
for line in f:
	word = line.strip().split('\t')
	if s in word[0]:
		g.write(line)
f.close()
f=open(sys.argv[2])
for line in f:
	word = line.strip().split('\t')
	if s not in word[0]:
		g.write(line)
		
