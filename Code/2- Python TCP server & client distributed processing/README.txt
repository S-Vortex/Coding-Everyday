Min-Max Distributed Processing (Python)
_______________________________________________________________

Details:
____________

Language:
	Python 3.4.1

IDE:
	Sublime text 3



Description:
____________
A homework assignment with two programs, a client and a server. The server is initiated three times, each on a different port. The client is initiated with the addresses of the servers as arguments as well as the number of numbers to generate. 

The client then sends the numbers to the servers one at a time (each server gets a third of them) and when it's done, sends a -1 integer to say that it's done. The servers then calculate the min, max, and standard deviation of the number lists they have. 

The servers then send these three data points back to the client as a string seperated by commas. The client accepts these strings and converts them into 3 lists, then calculates the lowest min and the highest max and then spits out the min, max, and the three standard deviations from the servers. 

The client then calculates on its own the min, max, and standard deviation for all of the numbers and prints this data to screen. 


The .bat file runs these files on seperate powershell windows on Windows 7+ machines. 


Server syntax:
	python server.py <port number>

Client syntax:
	Usage: python client.py <#integers> <First IP Address> <First Port> <Second IP> <Second Port> <Third IP> <Third Port>