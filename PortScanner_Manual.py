#!/usr/bin/python

import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%                                                         %%\n%%   #      #      #       #    #    #    #######   #   #  %%\n%%   ##    ##     # #      ##   #    #   #          #   #  %%\n%%   # #  # #    #   #     #  # #    #    ######    #####  %%\n%%   #  ##  #   #######    #   ##    #          #   #   #  %%\n%%   #      #  #       #   #    #    #   #######    #   #  %%\n%%                                                         %%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
#Salutaion to use
print("Welcome To Port Scanner Engine")
username=input("Please Enter Your Name:")
print("Hey,")
print(username)
print("\n")






hostname = input("[*]Enter host name (IP ADDRESS) : ")
portname = int(input("[*]Enter port number : "))
print ('...............SCANNING.................\n\n')
def portscanner(portname):
    if connection.connect_ex((hostname, portname)):
        print("[✘] Port %d is CLOSED\n" % (portname))
    else:
        print("[✔] Port %d is OPEN\n" % (portname))

portscanner(portname)
