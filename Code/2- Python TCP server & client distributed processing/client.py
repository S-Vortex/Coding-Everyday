#///////////////////////////////////////////////////////////////////////////////
#// Student: Sam Mills
#// Course: COSC 4653 - Advanced Networks
#// Assignment 1 - min-max-StdDev Distributed Processing
#//    Due date: Tuesday January 20, 2015
#//
#// Language: Python 3.4.1
#// File Name: client.py
#//
#// Programs Purpose:
#//   This client program connects to three instances of its corresponding
#//   server. It then iterates through a list of numbers, sending them to each
#//   server one at a time.
#//   After it's done, it receives from each server one packet containing the
#//   minimum, maximum, and standard deviation values for the 1/3 of the numbers
#//   that server received. This client then outputs a combined data set and 
#//   then computes the data itself over the whole set of numbers.
#//    
#// Programs limitations:
#//   Requires console arguments: 
#//       python client.py <#integers> <First IP Address><First Port>
#//       <Second IP> <Second Port> <Third IP> <Third Port> 
#//   Will exit if arguments were entered wrong.
#//   Will exit if any server is not reachable.
#//   May fail if unnaccounted for network traffic occurs
#//   Cannot combine standard deviation values, this is impossible
#//   Does not support domain names with a '-' character in them.
#//
#// Operating System: Windows 8.1
#// IDE: Sublime Text 3
#// Operational Status: Working
#// Developement Computer: Xeta (Sam Mills' surface pro 3)
#//////////////////////////////////////////////////////////////////////////////


#Open Libraries
import sys
import argparse
import re
from random import randint
from socket import *
import struct
import statistics

#==============================================================================
#=============================================================
#--                        Functions                        --
#=============================================================

#Converts the specified number into binary and sends it to the
#server in a single packet
def send_int(sock, num):
	packed_int = struct.pack("!i", num)
	sock.send(packed_int)

#Clean up my code by making this function do the dirty work of 
#deciding which server is next in line to receive a number. 
#In the while loop in the main code, there is an iteration counter
#that keeps track of what iteration the loop is on. 
#This mods that counter by 3 to give a continuously looping series of 
#0, 1, and 2. This is perfect for deciding which server gets a number
#next. It then uses the original send_int() function to push the
#current number through the right socket.
def send_int_simple(iteration, number_to_send):
	next_server = iteration % 3 # returns either 0,1, or 2
	if(next_server == 0):
		send_int(sock1, number_to_send)
		print('server 1')
	if(next_server == 1):
		send_int(sock2, number_to_send)
		print('server 2')
	if(next_server == 2):
		send_int(sock3, number_to_send)
		print('server 3')


#Sends a -1 to each server to signify that all of the numbers
#have been sent
def end_send():
	packed_int = struct.pack("!i", -1)
	sock1.send(packed_int)
	sock2.send(packed_int)
	sock3.send(packed_int)

#receives the specified amount of data
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def recv_one_message(sock):
    num_received, = struct.unpack('!i', recvall(sock, 4))
    returned2, = struct.unpack('50p',recvall(sock, num_received))
    return returned2

#receives the computed data from the servers as a string,
#comma separated, splits the string into integers, and puts 
#the integers into a list. It then returns this list. 
#  Order of list is as follows: [<min>, <max>, <std_dev>]
def recv_values(sock):
	bufflength = recvall(sock, 4)
	length = struct.unpack('s', bufflength)
	msg_string = recvall(sock, length)
	numberlist = map(float, msg_string.split(','))
	return recvall(sock, length)


#Combines the returned values into the final data
#There will be 5 values: Min, Max, and three std_devs
def combine(listA, listB, listC):
	#final list
	listD = []
	#set templist to be the min values
	tempList = [listA[0], listB[0], listC[0]]
	#set final list to be min of min values
	listD.append(min(tempList))
	#set templist to be the max values
	tempList = [listA[1], listB[1], listC[1]]
	#set final list to be min of max values
	listD.append(max(tempList))
	#Set the rest of the list to be the standard deviations
	#because we cannot combine them into one term
	listD.append(listA[2])
	listD.append(listB[2])
	listD.append(listB[2])
	#return the list
	return listD

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
#into a string ready to be displayed to the user
def format(numberlist):
    result_str =("Results computed by the client from data sent by"\
    " the servers:\n\nMinimun value: %f \nMaximum value: %f \n"\
    "Standard deviation values: %f, %f, %f" % (numberlist[0],\
    numberlist[1],numberlist[2],numberlist[3],numberlist[4]))
    return result_str

def format2(numberlist):
    result_str =("Results computed by the client from data sent by"\
    " the servers:\n\nMinimun value: %f \nMaximum value: %f \n"\
    "Standard deviation value: %f" % (numberlist[0],\
    numberlist[1],numberlist[2]))
    return result_str


#==============================================================================
#====================================================
#--                   Input                        --
#====================================================

#Make sure there are arguments
if(len(sys.argv)!=8):
	print("\nUsage: python client.py <#integers> <First IP Address>'\
		' <First Port> <Second IP> <Second Port> <Third IP> <Third Port>\n")
	exit()

#Parse input
parser = argparse.ArgumentParser(description='Get console input.')
parser.add_argument('count',\
	help='The count of numbers to generate (At least 3)')
parser.add_argument('address1', nargs=2, metavar=('ad', 'port'),\
	help='The first server address. Please input an IP address and a port'\
	'number seperated by a space for this argument.')
parser.add_argument('address2', nargs=2,metavar=('ad', 'port'),\
	help='The second server address. Please input an IP address and a port'\
	'number seperated by a space for this argument.')
parser.add_argument('address3', nargs=2,metavar=('ad', 'port'),\
	help='The third server address. Please input an IP address and a port'\
	'number seperated by a space for this argument.')

#Use args as the dictionary to make it easier
args = parser.parse_args()



#==============================================================================
#=========================================================================
#--     Get the values from the argument inputs and check validity      --
#=========================================================================

#set the number of integers to generate from the arguments and 
#   make sure it's an integer above three and less than a million
count = int(args.count)

if(int(count)<3 or int(count)>1000000):
	print("The first argument is the number of integers to generate and must be"\
		" at least 3 and less than 1,000,001")
	print("\nUsage: python client.py <#integers> <First IP Address>"\
		" <First Port> <Second IP> <Second Port> <Third IP> <Third Port>\n")
	exit()

#Assign arguments to more memorable variables
IP1 = args.address1[0]
IP2 = args.address2[0]
IP3 = args.address3[0]

port1 = int(args.address1[1])
port2 = int(args.address2[1])
port3 = int(args.address3[1])

#check IP's to make sure they are formatted correctly in IP4 format
r1 = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
r2 = re.compile('^localhost$', re.IGNORECASE)
r3 = re.compile('^(([a-z0-9]){1,63}\.?){1,255}$')
#This is a big if statement, checking 9 combinations
#That is, three arguments against three regexes. 
#if one regex set fails, program exits. 
if(((r1.match(IP1) is None) and (r2.match(IP1) is None) and (r3.match(IP1) \
	is None))\
or((r1.match(IP2) is None) and (r2.match(IP2) is None) and (r3.match(IP2) \
	is None))\
or((r1.match(IP3) is None) and (r2.match(IP3) is None) and (r3.match(IP3) \
	is None))):
		#end of the if statement finally
		print("\nThe second, fourth, and fifth arguments must be valid IP4"\
			" addresses in the form 0.0.0.0 or localhost or a domain name.")
		print("\nUsage: python client.py <#integers> <First IP Address> "\
			"<First Port> <Second IP> <Second Port> <Third IP> <Third Port>\n")
		exit()

#create tuples for server addresses
server1 = (IP1, port1)
server2 = (IP2, port2)
server3 = (IP3, port3)



#==============================================================================
#======================================
#--  Create sockets and connections  --
#======================================

# Create a TCP/IP socket
sock1 = socket(AF_INET, SOCK_STREAM)
sock2 = socket(AF_INET, SOCK_STREAM)
sock3 = socket(AF_INET, SOCK_STREAM)
serversock = socket(AF_INET, SOCK_STREAM)
serversock.bind(('localhost', 9999))

# Connect sockets to servers
print('\nConnecting to servers')
failed = 0
try:
	sock1.connect(server1)
	print('server 1 connected')
except:
	print('server 1 could not connect.')
	failed = 1

try:
	sock2.connect(server2)
	print('server 2 connected')
except:
	print('server 2 could not connect.')
	failed = 1

try:
	sock3.connect(server3)
	print('server 3 connected\n')
except:
	print('server 3 could not connect.\n')
	failed = 1

if(failed == 1):
	print('A server did not connect, quitting now.')
	exit()



#==============================================================================
#=================================
#--  Generate and send numbers  --
#=================================

#list to contain numbers
numbers = []
print('Generating %d numbers' % count)
for i in range(0,count):               #generate the specified amount of numbers
	numbers.append(randint(0,1000000))       #add the new number to list
numbers.append(-1)                        #finish the list with a -1
print('Done generating numbers.\n')

#Go through the list one number at a time until it reaches the end
#of the list. The end of the list is designated by a vale of -1.
#The numbers in the list are sent one by one to the next server in 
#line.
i=0           #iteration counter
while(numbers[i]!=(-1)):
	print('Sending number %d, which is %d' %(i,numbers[i]))
	send_int_simple(i, numbers[i])
	i += 1

#Tell the servers we are done
end_send()



#==============================================================================
#===================================
#--  receive and compute numbers  --
#===================================

#receive the returned string from each socket
return1 = str(recv_one_message(sock1)).strip( "'b" )
print("Received "+str(return1)+' from server 1\n')
return2 = str(recv_one_message(sock2)).strip( "'b" )
print("Received "+str(return2)+' from server 2\n')
return3 = str(recv_one_message(sock3)).strip( "'b" )
print("Received "+str(return3)+' from server 3\n')

#.translate(None, "'b")

#turn returned strings into lists
returnList1 = list(map(float, return1.split(',')))
returnList2 = list(map(float, return2.split(',')))
returnList3 = list(map(float, return3.split(',')))


#compute and print the combined data
result_list = combine(returnList1, returnList2, returnList3)
output_str = format(result_list)
print('\n\n' + output_str + '\n\n')

#compute and print out data from this client itself using the original list
result_list = compute(numbers)
output_str = format2(result_list)
print('\n\n' + output_str + '\n\n')