import os
import math

idf = dict()
words = []

with open('data/word1475.txt') as fp:
	for line in fp:
		# line = line.decode('big5').encode('utf-8')
		words.append(line.strip())

for file in sorted(os.listdir('data')):
	if file.endswith('.wrd'):
		with open('data/' + file) as fp:
			for line in fp:
				line = line.decode('big5').encode('utf-8').strip()
				word = line.split(' ')[0]
				if word in idf:
					idf[word] += 1.0
				else:
					idf[word] = 1.0

for word, value in idf.iteritems():
	idf[word] = 2 - math.log10(value)
	#print word + ' ' + str(idf[word])

for file in sorted(os.listdir('data')):
	if file.endswith('.wrd'):
		with open('data/' + file) as fp:
			total = 0
			# print file + ':'
			for line in fp:
				line = line.decode('big5').encode('utf-8').strip()
				if len(line) > 0:
					total += float(line.split(' ')[1])
			fp.seek(0)
			tfidf = dict()
			for line in fp:
				line = line.decode('big5').encode('utf-8').strip()
				if len(line) > 0:
					word = line.split(' ')[0]
					tf = float(line.split(' ')[1]) / total
					tfidf[word] = tf * idf[word]
			for word in words:
				if word in tfidf:
					print tfidf[word],
				else:
					print 0,
			print
