
import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
data = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

while 1:
   
    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))
    data_int = int(data)
    message = "Message"
    counter = 1;
    while counter <= data_int:
        sendMessage = message + str(counter)
        counter = counter + 1
        s.sendto(sendMessage.encode('utf-8'), server_address)

        
        print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

        buf, address = s.recvfrom(port)
            
        print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))

s.shutdown(1)

