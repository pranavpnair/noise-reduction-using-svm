import subprocess
import sys
h=open("values.tsv",'w')
s=str(sys.argv[1])
h.write('fraction'+'\t'+'noise at top' + '\t' + 'total data points' + '\t'+ 'positive data points' + '\t'+ 'negative data points'+ '\t' + 'positive noise points at top'+ '\t'+ 'negative noise points at top'+ '\t' +'total noise'+ '\n')
h.close()
i=0
a=[0.01,0.05,0.1,0.25,0.5]
while(i<5):
	subprocess.call('python dist_rect.py shoppinglist3.tsv '+s+' '+ str(a[i]), shell=True)
	subprocess.call('python ab.py '+s+' shoppinglist1.tsv shoppinglist.tsv',shell=True)
	i+=1
	j=0
	while(j<5):
		subprocess.call('''python main.py ''' + str(a[j]) +' '+s, shell = True) 
		j+=1
