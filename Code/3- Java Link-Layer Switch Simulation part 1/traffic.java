//Designed by Sam Mills
//Assignment 2: Link-Layer Switch Simulation – Part I (in Java)
//February 3, 2015
//Purpose: practice sending messages between two processes by way
//   of UDP packets and to practice implementing a ling-layer
//   simulation involving two processes
//Description: 
//   traffic.jar is a client process. It auto-generates an unending
//   source of link-layer frames and sends them at random times to
//   the switch simulator. These frames appear to be sent to the 
//   swith simulator from a variety of link-layer nodes (MAC 
//   addresses)

import java.util.*


public class traffic{

	// Listening port
	private int Port = 2323;

	public static void main(String[]args){
		//Handle args and set values
		String IPAddress = args[0];
		int serverPort = args[1];
		String fileName = args[2];
		int maxInterval = args[3];

		//


	}

	public void readFile(String filename){
		//Make a buffered reader to read the file
		BufferedReader buffer = new 
			BufferedReader(new FileReader(filename));

		String line;
		int count = 0;

		while((line = buffer.readLine()) != null){
			
		}
	}


}

