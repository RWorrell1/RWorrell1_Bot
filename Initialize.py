import string
from Socket import sendMessage
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(2048)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	sendMessage(s, "Successfully Joined Chat")
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True