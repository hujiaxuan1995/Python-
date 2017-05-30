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
		filesize = 1024 * size
	


def textGen():
	global filesize
	ds = 0
	f = open("../vocabulary",'r')
	buffer = f.read()
	f.close()

	# print buffer

	count = int(buffer.split("\n")[0])
	words_ = buffer.split("\n")[1].split(',')

	for i,word in enumerate(words_):
		words_[i] = word.strip()
	print outpath
	with open(outpath,'w') as fout :

		index = 1;
		#print filesize
		while ds < filesize:
			item = int(random.random() * count)
			str = words_[item]
			fout.write(str)
			fout.write(' ')
			if((index%10) == 0):
				fout.write('\n')
			index += 1 
			ds = os.path.getsize(outpath)
			# print ds
		fout.close()
		print filepath
		print outpath
	

if __name__ == "__main__":

	s = "   hello"
	
	scala = ''
	size = 0
	
	if(len(sys.argv) == 3):
		scala = sys.argv[1]
		size = int(sys.argv[2])
	if(len(sys.argv) == 2):
		size = int(sys.argv[1])
	filepath = '../vocabulary'
	outpath = '../data/text1.txt'

	genSize(scala,size)
	textGen()
