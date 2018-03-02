#! #!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from sklearn.metrics import cohen_kappa_score

annotator1_emotion = []
annotator2_emotion = []
annotator1_caused_language = []
annotator2_caused_language = []

with open('annotation1.tsv') as dataset1:
	for line in csv.reader(dataset1, delimiter="\t" ):
		text = line[0]
		if len(line[1]) > 0:
			annotator1_emotion.append("Happiness")
			annotator1_caused_language.append(line[1])
		elif len(line[2]) > 0:
			annotator1_emotion.append("Sadness")
			annotator1_caused_language.append(line[2])
		elif len(line[3]) > 0:
			annotator1_emotion.append("Anger")
			annotator1_caused_language.append(line[3])
		elif len(line[4]) > 0:
			annotator1_emotion.append("Fear")
			annotator1_caused_language.append(line[4])
		elif len(line[5]) > 0:
			annotator1_emotion.append("Disgust")
			annotator1_caused_language.append(line[5])
		elif len(line[6]) > 0:
			annotator1_emotion.append("Surprise")
			annotator1_caused_language.append(line[6])

with open('annotation2.tsv') as dataset2:
	for line in csv.reader(dataset2, delimiter="\t" ):
		text = line[0]
		if len(line[1]) > 0:
			annotator2_emotion.append("Happiness")
			annotator2_caused_language.append(line[1])
		elif len(line[2]) > 0:
			annotator2_emotion.append("Sadness")
			annotator2_caused_language.append(line[2])
		elif len(line[3]) > 0:
			annotator2_emotion.append("Anger")
			annotator2_caused_language.append(line[3])
		elif len(line[4]) > 0:
			annotator2_emotion.append("Fear")
			annotator2_caused_language.append(line[4])
		elif len(line[5]) > 0:
			annotator2_emotion.append("Disgust")
			annotator2_caused_language.append(line[5])
		elif len(line[6]) > 0:
			annotator2_emotion.append("Surprise")
			annotator2_caused_language.append(line[6])

#print annotator1_emotion
#print annotator1_caused_language
#print annotator2_emotion
#print annotator2_caused_language
print "Emotion Inter Annotator Agreement", cohen_kappa_score(annotator1_emotion, annotator2_emotion)
print "Caused Language Inter Annotator Agreement",cohen_kappa_score(annotator1_caused_language, annotator2_caused_language)