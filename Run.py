import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
import urllib2

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
				s.send("PONG " + "\r\n")
                print("Pong")
                
                user = getUser(line)
                message = getMessage(line)
            
            #start of Commands
                if "!donate" + "user-type=mod" in message:
                    sendMessage(s, user + " You Can Donate here http://www.streamtip.com/t/rworrell1 Min: $3")
                else:
                        sendMessage(s, user + " That Commands is For Mods Only")
                    
                if "hi" in message:
                    sendMessage(s, user + " Welcome To The Stream HeyGuys ")
                    
                if "hey" in message:
                    sendMessage(s, user + " Welcome To The Stream HeyGuys ")
                    
                if "!crew" in message:
                    sendMessage(s, user + " Join my crew at socialclub.rockstargames.com/crew/rworrell1")
                    
                if "!email" in message:
                    sendMessage(s, user + " email me at rworrell1gaming@gmail.com")
                    
                if "!psn" in message:
                    sendMessage(s, user + " My PSN Is ryandude21")
                    
                if "!site" in message:
                    sendMessage(s, user + " My site is rworrell1.weebly.com")
                    
                if "!steam" in message:
                    sendMessage(s, user + " My Steam Is NightTimeBurialMan")
                    
                #if "!sub" in message:
                    #sendMessage(s, "Sorry i dont have a sub button ")
                    
                if "!twitter" in message:
                    sendMessage(s, user + " twitter.com/rworrell1gaming")
                    
                if "!commands" in message:
                    sendMessage(s, user + " The Commands Are !donate, !crew, !email, !psn, !site, !steam")
            #End Of Commands
                    
            #Start Of Timeouts And Bans
                if ".com" in message:
                     sendMessage(s, ".timeout " + user + " 180")
                        
                if ".net" in message:
                     sendMessage(s, ".timeout " + user + " 180")
                        
                if ".gov" in message:
                     sendMessage(s, ".timeout " + user + " 180")
                
                if ".edu" in message:
                     sendMessage(s, ".timeout " + user + " 180")
                        
                if "porn" in message:
                    sendMessage(s, ".ban " + user)
                    
                if "Porn" in message:
                    sendMessage(s, ".ban " + user)
                    
                if "pornhub.com" in message:
                    sendMessage(s, ".ban " + user)
                    
                if "porn.com" in message:
                    sendMessage(s, ".ban " + user)
                    
                if "youporn.com" in message:
                    sendMessage(s, ".ban " + user)
                    
                if "abdulaporn.com" in message:
                    sendMesssage(s, ".ban " + user)
                    
                if "redtube.com" in message:
                    sendMesssage(s, ".ban " + user)
                    
                if "dinotube.com" in message:
                    sendMesssage(s, ".ban " + user)
            #End Of Timeouts And Bans