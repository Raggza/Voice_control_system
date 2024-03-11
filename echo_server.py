from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
from motorModule2 import Motor
import sys
import keyboardModule as kp
		
motor = Motor(23,24,25,17,27,22)
PORT_NUMBER = 5000
SIZE = 1024
hostName = gethostbyname( '0.0.0.0' )
mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )
print ("Test server listening on port {0}\n".format(PORT_NUMBER))
		
def main():
	(data,addr) = mySocket.recvfrom(SIZE)
	str1 = data.decode('utf-8')
	if str1 == 'lên':
		motor.move(0.6,0,0.1)
	elif str1 == 'xuống':
		motor.move(-0.6,0,0.1)
	elif str1 == 'trái':
		motor.move(0.5,0.3,0.1)
	elif str1 == 'phải':
		motor.move(0.5,-0.3,0.1)
	elif str1 == 'stop':
		motor.stop(0.1)
			
if __name__ == '__main__': 
	while True:
		main 