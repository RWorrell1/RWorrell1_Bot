import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
	
	irc = socket.socket()
	irc.connect((HOST, PORT))
	irc.send("PASS " + PASS + "\r\n")
	irc.send("NICK " + IDENT + "\r\n")
	irc.send("JOIN #" + CHANNEL + "\r\n")
        irc.send("CAP REQ :twitch.tv/tags" + "\r\n")
        irc.send("CAP REQ :twitch.tv/membership" + "\r\n")
        irc.send("CAP REQ :twitch.tv/commands" + "\r\n")
	return irc
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)
