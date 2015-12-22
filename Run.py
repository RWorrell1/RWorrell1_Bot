import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom


s = openSocket()
joinRoom(s)
readbuffer = ""


while True:
		readbuffer = readbuffer + s.recv(2048)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break
			user = getUser(line)
			message = getMessage(line)
			print user + " typed :" + message
            
                if "!donate" in message:
                    sendMessage(s, "You Can Donate here http://www.streamtip.com/t/rworrell1 Min: $3 ")
                    
                if "hi" in message:
                    sendMessage(s, "Welcome To The Stream HeyGuys ")
                    
                if "hey" in message:
                    sendMessage(s, "Welcome To The Stream HeyGuys ")
                    
                if "!crew" in message:
                    sendMessage(s, "Join my crew at socialclub.rockstargames.com/crew/rworrell1 ")
                    
                if "!email" in message:
                    sendMessage(s, "email me at rworrell1gaming@gmail.com ")
                    
                if "!psn" in message:
                    sendMessage(s, "psn=ryandude21 ")
                    
                if "!site" in message:
                    sendMessage(s, "My site is rworrell1.weebly.com ")
                    
                if "!steam" in message:
                    sendMessage(s, "NightTimeBurialMan ")
                    
                #if "!sub" in message:
                    #sendMessage(s, "Sorry i dont have a sub button ")
                    
                if "!twitter" in message:
                    sendMessage(s, "twitter.com/rworrell1gaming ")
                    
                if "!commands" in message:
                    sendMessage(s, "!donate, !crew, !email, !psn, !site, !steam ")
                    