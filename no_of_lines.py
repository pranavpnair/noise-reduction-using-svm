import sys
f=open(sys.argv[1])
i=0
k=0
for line in f:
	w=line.strip().split('\t')
	if 'Grocery' in w[0]:
		k=k+1
	i=i+1
print(k,i)
