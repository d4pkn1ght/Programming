#!usr/bin/python
import os
import random

def remake():
	path = "C:\\Users\\DELL\\Desktop\\TEST\\"
	files = os.listdir(path)

	for file in files:
		rand = random.randrange(0,9999)
		filePath = path + 'I LOVE YOU_{0} - [{1}]'.format(rand, file)
		os.rename(path + file, filePath)

if __name__ == "__main__":
	remake()
