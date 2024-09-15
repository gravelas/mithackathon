import serial
import math

isSatelite = False
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)

def initSocket(socket, endpoint, port):
    ser.write(('AT%SOCKETCMD="DELETE",' + socket + '\r\n').encode("UTF-8"))
    ser.read_until()
    ser.read_until()
    ser.write(('AT%SOCKETCMD="ALLOCATE",' + socket + ',"UDP","OPEN","' + endpoint + '",'+ port +',0\r\n').encode("UTF-8"))
    ser.read_until()
    ser.read_until()

    ser.write(('AT%SOCKETCMD="ACTIVATE",' + socket + '\r\n').encode("UTF-8"))
    ser.read_until()
    ser.read_until()
    ser.read_until()
    ser.read_until()
    

def sendPacket(socket, packet: str):
    packet = packet.encode("utf-8").hex()
    size = math.trunc(len(packet)/2)
    sizeStr = str(size)
    ser.write(('AT%SOCKETDATA="SEND",' + socket + ',' + sizeStr + ',"' + packet + '"\r\n').encode("UTF-8"))
    ser.read_until()
    ser.read_until()
    ser.read_until()
    ser.read_until()
    ser.read_until()
    ser.read_until()
    ser.read_until()


def switchToSatelite(socket):
    ser.write(('AT%RATACT="NBNTN","'+socket+'"').encode("UTF-8"))
    global isSatelite 
    isSatelite = True
    print(ser.read_until())
    print(ser.read_until())
    print(ser.read_until())
    print(ser.read_until())    

def switchToCellular(socket):
    ser.write(('AT%RATACT="CATM","'+socket+'"').encode("UTF-8"))
    ser.write(('ATZ').encode('utf-8'))
    global isSatelite 
    isSatelite = False
    print(ser.read_until())
    print(ser.read_until())
    print(ser.read_until())
    print(ser.read_until())

initSocket("1", "97.107.140.69", "12345")

while True:
    print("isSatelite? " + str(isSatelite))
    print("1) Message")
    print("2) Switch to Satelite")
    print("3) Switch to Cellular")
    answer = input()
    if (answer == "1"):
        print("Message:", end=" ")
        message = input()
        sendPacket("1", message)
    elif (answer == "2"):
        switchToSatelite("1")
    elif (answer == "3"):
        switchToCellular("1")


#initSocket("1", "97.107.140.69", "12345")

#sendPacket("1", "48656C6C6F2C20776F726C64216920686f7065207468697320776f726b730d0a0d0a")

