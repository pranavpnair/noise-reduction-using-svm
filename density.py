import sys
x=0
y=0
f=open(sys.argv[1])	#noise_lines
g=open(sys.argv[2])	# support vectors
h=open(sys.argv[3]) # data file
a=[]
bucket=0
t=0
i=0
for line in h:
	t=t+1
for line in f:
	a.append(int(float(line.strip()))-1)
for line1 in g:
	bucket+=1
	line=line1.strip()
	q=line.strip('()').split(',')
	w=int(q[0])
	d=int(q[2])
	if(w in a and d==1):
		x+=1
		i+=1
	elif(w in a and d==-1):
		y+=1
		i+=1
	if(bucket>=0.05*t):
		print((i,x,y))
		x=0
		i=0
		y=0
		bucket=0
		
	
		
	


