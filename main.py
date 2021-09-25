import subprocess
import os
import time
import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("    ____      ____  _                             ____      __                    ")
print("   /  _/___  / __ \(_)___  ____ ____  _____      / __ \____/ /___  ________  _____")
print("   / // __ \/ /_/ / / __ \/ __ `/ _ \/ ___/_____/ / / / __  / __ \/ ___/ _ \/ ___/")
print(" _/ // /_/ / ____/ / / / / /_/ /  __/ /  /_____/ /_/ / /_/ / /_/ (__  )  __/ /    ")
print("/___/ .___/_/   /_/_/ /_/\__, /\___/_/        /_____/\__,_/\____/____/\___/_/     ")
print("   /_/                  /____/                                                    ")
print("")
print("Your local IP address is " + host_ip + ".")
print("Name of this system is ,," + host_name + "''.")
print("")
print("")
ipaddress = input("Type IP address to ping: ")
times = input("How many times to ping? [Press 0 for infinite ping]")
while True:
    os.system('ping -n ' + times + ' {}'.format(ipaddress))
    time.sleep(10)
    exit()

    if times == "0":
        os.system('ping -n 429290 {}'.format(ipaddress))
