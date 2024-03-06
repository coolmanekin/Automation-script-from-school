###############NETWORK HOMEWORK######################
##### CSEC-380/480 Security Automation - Ryan Haley####
'''
You have just joined an elite 3-letter government agency’s red team.
On your first assignment, you gain access to a host on the target network,
but are unable to upload or run any unauthorized tools due to strict
application control on the host. You do notice, however, that python is
a whitelisted application on the host. Knowing this, you decide to use
it to do your reconnaissance (scanning) of the network.
 
Create a program that simulates nmap (network scanning tool).
Your program must accept options for IP(s), TCP or UDP,
and port numbers or ranges. The program will then tell the
user which ports are open on the target IP(s). 

You are to scan your Windows 10 host (10.12.0.15) from your Kali system (10.12.0.10) ONLY!!!

Required Conditions (0.75 pts/each - 5 pts total):
	Does it run without errors? 
	Can it successfully scan 1 IP? 
	Can it successfully scan multiple IPs? 
	Can it attempt to identify open/closed UDP ports? 
	Can it identify open/closed TCP ports? 
	Can it successfully scan multiple ports? 
	Does it properly inform the user of findings? 

Bonus Conditions (+3.5 possible):
	Fingerprint any port/service running a webserver (What service and version was discovered). (0.5 pt)
                Inform the user of the type and version server found. (0.5pts)
                If Service is a webserver:
                        Inform the user of the status code returned (for a root request – aka "GET / HTTP/1.1"). (0.5pts)
                        Inform the user of the title of the page found. (0.5pts)
	Option to take a list (txt file) of IPs to scan. (0.5 pts)
	Option to take a timeout value between each port scan. (0.5 pts)
	Option to save results to a  txt file (0.5 pts)
'''

import socket

def check_port(host, port, protocol):
    try:
        if protocol == 'TCP':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
        elif protocol == 'UDP':
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
    except Exception as e:
        print(e)
        return False

def scan_ports(host, ports, protocol):
    open_ports = []
    for port in ports:
        if check_port(host, port, protocol):
            open_ports.append(port)
    return open_ports

def main():
    host = input("Enter the host(s) IP seperated by Semicolon:(Ex.10.0.0.1;10.0.0.2 etc")
    hostLst = host.split(";")
    protocol = input("Enter the protocol (TCP/UDP): ")
    port_range = input("Enter the port range (e.g. 1-1024): ")
    start_port, end_port = map(int, port_range.split('-'))
    ports = range(start_port, end_port + 1)
    for ip in hostLst:
        open_ports = scan_ports(ip, ports, protocol)
        print("Open ports on host %s: %s" % (ip, open_ports))

if __name__ == '__main__':
    main()
