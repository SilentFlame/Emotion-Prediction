import csv
text_id = 2
id_to_tweet_map = {}
tweet_to_id_map = {}
id_to_emotion_map = {}
id_to_caused_language_map = {}
empty_emotions = 0
with open('dataset.tsv') as dataset:
	for line in csv.reader(dataset, delimiter="\t"):
		
		emotions = []
		caused_language = []
		text = line[0]
		if len(line[1]) > 0:
			emotions.append("Happiness")
			caused_language.append(line[1])
		if len(line[2]) > 0:
			emotions.append("Sadness")
			caused_language.append(line[2])
		if len(line[3]) > 0:
			emotions.append("Anger")
			caused_language.append(line[3])
		
		if len(line[4]) > 0:
			emotions.append("Fear")
			caused_language.append(line[4])
		if len(line[5]) > 0:
			emotions.append("Disgust")
			caused_language.append(line[5])
		if len(line[6]) > 0:
			emotions.append("Surprise")
			caused_language.append(line[6])
		
		id_to_tweet_map[text_id] = text
		tweet_to_id_map[text] = text_id
		id_to_emotion_map[text_id] = emotions
		id_to_caused_language_map[text_id] = caused_language


		#if len(emotions) == 0:
			#empty_emotions = empty_emotions + 1
			#print text_id, text
		#text_id = text_id + 1



#print id_to_tweet_map[1454]
#print tweet_to_id_map['Live aane ke liye switch to #JIO services !!!']
#print id_to_emotion_map[1454]
#print id_to_caused_language_map[1454]

#print empty_emotions
