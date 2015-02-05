#///////////////////////////////////////////////////////////////////////////////
#// Student: Sam Mills
#// Course: COSC 4653 - Advanced Networks
#// Assignment 1 - min-max-StdDev Distributed Processing
#//    Due date: Tuesday January 20, 2015
#//
#// Language: Python 3.4.1
#// File Name: server.py
#//
#// Programs Purpose:
#//   This server program receives a connection from the client program and then
#//   receives numbers one at a time which it must add to a list and compute the
#//   lists min, max, and standard deviation. It saves these three values in a 
#//   comma seperated string and sends this string back to the client.
#//    
#// Programs limitations:
#//   Requires console arguments: 
#//       python server.py <port number>
#//   May fail if unnaccounted for network traffic occurs
#//
#// Operating System: Windows 8.1
#// IDE: Sublime Text 3
#// Operational Status: not working
#// Developement Computer: Xeta (Sam Mills' surface pro 3)
#//////////////////////////////////////////////////////////////////////////////


#Open Libraries
import sys
import argparse
import re
from socket import *
import struct
import statistics


#====================================================
#--                   Input                        --
#====================================================
#Make sure there are arguments
if(len(sys.argv)!=2):
	print("\nUsage: python server.py <port number>\n")
	exit()

#Parse input
parser = argparse.ArgumentParser(description='Get console input.')
parser.add_argument('port', help='The port number to run the server on')
args = parser.parse_args()
port = int(args.port)



#=================================
#--  Number list and variables  --
#=================================

#Number list
num_list = []


#======================================
#--  Create sockets and connections  --
#======================================

# Create a TCP/IP socket
serversock = socket(AF_INET,SOCK_STREAM)
buffersize = 4

# Bind the socket to the port
server_address = ('localhost', port)
serversock.bind(server_address)
print ('server starting up on %s port %s' % server_address)

# Listen for incoming connections
serversock.listen(1)
print("Socket listening")



#=============================================================
#--                        Functions                        --
#=============================================================

#receives the specified amount of data
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

#receive one message
def recv_one_message(sock):
    lengthbuf = int(recvall(sock, 4))
    length = struct.unpack('!i', lengthbuf)
    return str(recvall(sock, length))

#receive one integer
def recv_one_integer(sock):
	num_received = struct.unpack('!i', recvall(sock, 4))
	num_received_num = num_received[0]
	return num_received_num

#send the string
def send_one_message(sock, data):
    data = bytes(data, 'utf-8')
    length = len(struct.pack('50p', data))
    sock.sendall(struct.pack('!i', length))
    sock.sendall(struct.pack('50p', data))


#Computes the min, max, and std_dev of a list and returns
#the results as a list
def compute(numberlist):
	#final list
	results = []
	#set first number to min of list
	results.append(min(numberlist))
	#second number is max
	results.append(max(numberlist))
	#third is std_dev
	results.append(float(statistics.stdev(numberlist)))

	#return the results
	return results

#Takes the computed data in the form of a list and puts it
#into a string of data to send back to client
def format(numberlist):
	if(len(numberlist) == 3):
		print("Computed data (min, max, std_dev)\n  " + str(numberlist))
		result_str =("%d, %d, %F" % (int(numberlist[0]), int(numberlist[1]), \
			float(numberlist[2])))
	else:
		result_str = "The wrong list was inputted to formatter"
	return result_str


#===============================================================
#--                        Connections                        --
#===============================================================
#Wait for connections
data = 1
count = 0
connection, address = serversock.accept()

while (True):
	count += 1
	data = recv_one_integer(connection)
	if(data == -1):
		print('received quit command\n')
		break
	else:
		num_list.append(data)
		print('recieved %d \n' % data)



#===============================
#--      compute and send     --
#===============================

#compute data from list
results = compute(num_list)
#turn the results into a string to make sending back to client easier
results_str = str(format(results))


#send the string over the socket
print("\nSending result string seperated by commas:\n   '" + results_str + "'\n")
send_one_message(connection, results_str)
print("String converted to bytes and sent.\n")
