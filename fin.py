import os
from operator import itemgetter

files = []

for file in sorted(os.listdir('data')):
	if file.endswith('.txt'):
		files.append(file)

def printfile(filename, keyword):
	with open('data/' + filename) as printingfilename:
		print 'data/' + filename
		for line in printingfilename:
			line = line.decode('big5').encode('utf-8')
			line = line.replace(keyword, '\033[91m' + keyword + '\033[0m')
			print line,
	print '-----------------'

print 'Welcome to the search engine.'
print 'Type one keyword and I can search docs for you.'
print 'Use Ctrl-C or Ctrl-D to exit.'
print '''
`7MMF'`7MM"""Mq.  
  MM    MM   `MM. 
  MM    MM   ,M9  
  MM    MMmmdM9   
  MM    MM  YM.   
  MM    MM   `Mb. 
.JMML..JMML. .JMM.
'''

while(True):
	word = raw_input('input keyword:')

	with open('data/word1475.txt') as fp:
		i = 0
		found = False
		for line in fp:
			if line.strip() == word:
				found = True
				break;
			i += 1
	if found != True:
		print 'Sorry, no such keyword.'
		continue
	else:
		idx = i
		listRank = dict()
		with open('weight1.txt') as fp:
			i = 0
			for line in fp:
				words = line.strip().split(' ')
				if float(words[idx]) > 0:
					listRank[i] = words[idx]
				i += 1
		listRank = sorted(listRank.items(), key=itemgetter(1), reverse=True)
		for doc in listRank:
			# print doc
			printfile(files[doc[0]], word)
		print str(len(listRank)) + ' results in total.'
				
