# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
data = sys.arg[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

while 1:
    data_int = int(data)
    message = "Message"
    counter = 1;
    while counter <= data_int:
        sendMessage = message + str(counter)
        counter = counter + 1
        s.sendto(sendMessage.encode('utf-8'), server_address)
        while True:

            print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

            buf, address = s.recvfrom(port)
                if not len(buf):
            break
            print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))

s.shutdown(1)

