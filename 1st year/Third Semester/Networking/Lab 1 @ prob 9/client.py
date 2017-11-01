#import socket for all socket related primitives
import socket
# we need struct in order to be able to pack data in
# a stream of bytes so that we can actually send
# an integer as a binary four byte sequence - instead
# of a string
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( ("192.168.30.128",1234) )

list1 = []
list2 = []

print("The first list :")
while(1):
    a = int(input(""))
    if a == 0:
        break
    list1.append(a)

res = s.send(struct.pack("!H", len(list1))) #for better performance, send it before we read the second list
for i in list1:
    res = s.send(struct.pack("!H", i))

print("The second list :")
while(1):
    a = int(input(""))
    if a == 0:
        break
    list2.append(a)

res = s.send(struct.pack("!H", len(list2)))
for i in list2:
    res = s.send(struct.pack("!H", i))


lengthOfArray = s.recv(2)

# unpack the content read from the network into a short int
# and convert from network representation back to host
lengthOfArray = struct.unpack('!H', lengthOfArray)

length = lengthOfArray[0]

print("The uncommon elements are : ")
while length:
    elements = s.recv(2)
    elements = struct.unpack('!H', elements)
    print(elements[0].__format__('d'))
    length -= 1

s.close()