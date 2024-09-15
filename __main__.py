# run with python3

import socketserver  # we use the socketsever module that comes with python3
import SensorLife

class MyUDPHandler(socketserver.DatagramRequestHandler):

	def handle(self):
		print("Got an UDP Message from {}".format(self.client_address[0]))

    	# for line terminated massages
		msgRecvd = self.rfile.readline().strip()
		global sensor
		sensor.message_recieved(msgRecvd.decode('utf-8'))
		print(msgRecvd.decode('utf-8'))

    # with receive buffer - reads max 1024 bytes
    # rec_bytes = self.request.recv(1024)
    # your processing here

# this is the main entrypoint
if __name__ == '__main__':
    # we specify the address and port we want to listen on
	listen_addr = ('0.0.0.0', 12345)
	global sensor
	sensor = SensorLife.SensorType()

    # with allowing to reuse the address we dont get into problems running it consecutively sometimes
	socketserver.UDPServer.allow_reuse_address = True 

    # register our class
	serverUDP = socketserver.UDPServer(listen_addr, MyUDPHandler)
	serverUDP.serve_forever()
