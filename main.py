"""
usage base64-tools <command> <extras>

comands:
-e <string> - encode string
-d <string> - decode string
-ef <filename> - encode file
-df <filename> - decode file
"""

import sys,base64

def encode(message):
	medium=message.encode("UTF-8")
	encodeMessage=base64.b64encode(medium)
	finalMessage=encodeMessage.decode("UTF-8")
	return finalMessage

def decode(encodeMessage):
	medium=base64.b64decode(encodeMessage)
	finalMessage=medium.decode("UTF-8")
	return finalMessage

def encodeFile(filename):
	with open(filename, 'r') as fileobj:
		with open(("encode-"+filename),"w") as fileobj2:
			lines=fileobj.readlines()
			for i in range(len(lines)):
				fileobj2.write(encode(lines[i])+"\n")

def decodeFile(filename):
	with open(filename,"r") as fileobj:
		with open("decode-"+filename,"w") as fileobj2:
			lines=fileobj.readlines()
			for i in range(len(lines)):
				fileobj2.write(decode(lines[i]))

if __name__ == '__main__':
	if(len(sys.argv)==1):
		print(__doc__.strip())
	else:
		if(sys.argv[1]=="-e"):
			print(encode(sys.argv[2]))
		elif(sys.argv[1]=="-d"):
			print(decode(sys.argv[2]))
		elif(sys.argv[1]=="-ef"):
			encodeFile(sys.argv[2])
		elif(sys.argv[1]=="-df"):
			decodeFile(sys.argv[2])