#!/usr/bin/python3
import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<---------------------------------------------->")

ip_addr = input("Please enter the IP adress you want to scan:")
print("Enter the IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan""")

print("You have selected option", resp)

if resp == "1":
  print("Nmap Version: ", scanner.nmap_version())
  scanner.scan(ip_addr, "1-1024", "-v -sS")
  print(scanner.scaninfo())
  print("IP Status: ", scanner[ip_addr].state())
  print(scanner[ip_addr].all_protocols())
  print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
  print("Nmap Version: ", scanner.nmap_version())
  scanner.scan(ip_addr, "1-1024", "-v -sU")
  print(scanner.scaninfo())
  print("IP Status: ", scanner[ip_addr].state())
  print(scanner[ip_addr].all_protocols())
  print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
  port_range = input("Please enter the range of UDP ports you want to scan:")
  print("Nmap Version: ", scanner.nmap_version())
  #task allow user to enter the range of ports for scan UDP ports
  scanner.scan(ip_addr, port_range, "-v -sS -sV -sC -A -O")
  print(scanner.scaninfo())
  print("IP Status: ", scanner[ip_addr].state())
  print(scanner[ip_addr].all_protocols())
  print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp >= "4":
  print("Please, enter the valid option.")
