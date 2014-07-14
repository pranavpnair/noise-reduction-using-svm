import subprocess
import sys
i=float(sys.argv[1])    #noise percentage
j=str(sys.argv[2])      #positive class name
o=open("shoppinglist.tsv")
h=open("values.tsv",'a')
subprocess.call('python intro_noise_percentage.py shoppinglist.tsv shoppingListWithNoise.tsv ' + str(i) + ' '+ j,shell=True)
subprocess.call('python models_predict.py shoppingListWithNoise.tsv '+ j+ ' >support_vectors',shell=True)
subprocess.call('python density.py noise_lines support_vectors shoppingListWithNoise.tsv > density',shell=True)
f=open("density")
line1=f.readline().strip()
w=line1.strip('()').split(',')
k=float(w[0])
g=open("noise_lines")
p=0
pos=0
neg=0
for line in o:
	words = line.strip().split('\t')
	if j in words[0]:
		pos+=1
	else:
		neg+=1	
for line in g:
	p+=1
h.write(str(k/p)+'\t' + str(k) + '\t'+ str(pos+neg) +'\t'+ str(pos) +'\t'+ str(neg) +'\t' + str(w[1]) +'\t'+ str(w[2]) +'\t'+ str(p) +'\n')

