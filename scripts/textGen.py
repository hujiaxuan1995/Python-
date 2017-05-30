import random
import os
import sys

global filesize

filesize = 0
filepath = ''
outpath = ''

def genSize(d,size):
	global filesize
	if d == 'M':
		filesize = 1 * 1024 * 1024 * size
	elif d == 'G':
		filesize = 1 * 1024 * 1024 * 1024 * size
	else : 
		filesize = size
	


def textGen():
	global filesize
	ds = 0
	f = open("../vocabulary",'r')
	buffer = f.read()
	# print buffer

	count = int(buffer.split("\n")[0])
	words_ = buffer.split("\n")[1].split(',')
	for i,word in enumerate(words_):
		words_[i] = word.strip()
	# r = []
	# for j in range(1000):
	# 	r.append(int(random.random()*count))

	f.close()
	with open("../text1.txt",'w') as fout :

		index = 1;
		print filesize
		while ds < filesize:
			item = int(random.random() * count)
			str = words_[item]
			fout.write(str)
			fout.write(' ')
			if((index%10) == 0):
				fout.write('\n')
			index += 1 
			ds = os.path.getsize(outpath)
			
		fout.close()
	
	

if __name__ == "__main__":

	s = "   hello"
	scala = sys.argv[1]
	size = int(sys.argv[2])
	filepath = '../vocabulary'
	outpath = '../text1.txt'
	genSize(scala,size)

	textGen()
