import os

words = []

with open('data/word1475.txt') as fp:
	for line in fp:
		# line = line.decode('big5').encode('utf-8')
		words.append(line.strip())

for word in words:
    for file in sorted(os.listdir('data')):
        if file.endswith('.wrd'):
            with open('data/' + file) as fp:
                found = False
                for line in fp:
                    line = line.decode('big5').encode('utf-8')
                    if word not in line:
                        continue
                    else:
                        found = True
                        break
            if found:
                print 1,
            else:
                print 0,
    print
