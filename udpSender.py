# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

while 1:
    print ("Enter how many messages you'd like to send: ENTER to quit")
    data = sys.stdin.readline().strip()
    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))

    message = "Message"
    counter = 1;
    while counter <= data:
        sendMessage = message + counter
        counter = counter + 1
        s.sendto(sendMessage.encode('utf-8'), server_address)

s.shutdown(1)

