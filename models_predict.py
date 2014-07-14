import sys
from collections import defaultdict

import numpy

from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.svm import LinearSVC
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score 
from sklearn.dummy import DummyClassifier

w=str(sys.argv[2])

def readExamples(inputFilename):
	queries = []
	labels = []
	first = False
	with open(inputFilename) as inputFile:
		for line in inputFile:
			if first:
				first = False
			else:
				words = line.strip().split('\t')
				query = words[2]
				if w in words[0]:
					label = 1
				else:
					label = 0
				labels.append(label)
				queries.append(query)
	return numpy.array(queries), numpy.array(labels)

def computeDensity(vectorizer, examples):
    nonZeros  = numpy.apply_along_axis(numpy.sum,1,vectorizer.transform(examples).todense())
    return 1 - numpy.count_nonzero(nonZeros)/float(len(nonZeros))

def predict(model,normalizer,vectorizer,examples, actual, fold=0, dump=False):
	X = normalizer.transform(vectorizer.transform(examples))
	pred = model.predict(X)
	return accuracy_score(actual,pred)

def predictF1(model,normalizer,vectorizer,examples, actual):
    X = normalizer.transform(vectorizer.transform(examples))
    pred = model.predict(X)
    return f1_score(actual,pred)

def prettyPrint(givenVector):
    return "%.4f" % givenVector.mean() +  "(" +"%.4f" % givenVector.std() + ")"    

examples, labels = readExamples(sys.argv[1])
folds = 10
trainingAccuracy = numpy.zeros(folds)
trainingBaseline = numpy.zeros(folds)
testingAccuracy = numpy.zeros(folds)
testingBaseline = numpy.zeros(folds)
testingDensity = numpy.zeros(folds)
testingF1 = numpy.zeros(folds)


vectorizer = CountVectorizer(min_df=1,dtype='double')
normalizer = Normalizer()
classifier = LinearSVC(loss='l1')
X = normalizer.fit_transform(vectorizer.fit_transform(examples))
y = labels
classifier.fit(X, y)
distance=[]
distance1 = classifier.decision_function(X)
p=0
for d in distance1:
	if d>=0:
		distance.append((p,abs(d),1))
	else:
		distance.append((p,abs(d),-1))
	p+=1 
distance.sort(key=lambda x:x[1])
for i in distance:
	print str(i)


