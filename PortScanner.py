'''
reqired nmap
if using windwos install nmap from website (https://nmap.org/download) 
using Linux >> sudo apt install nmap
and insall libarary >> pip3 install python-nmap
'''
import nmap

nm = nmap.PortScanner()

target = "127.0.0.1"
options = "-sV -sC scan_results"

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocal in nm[host].all_protocols():
        print("protocal: %s" % protocal)
        port_info = nm[host][protocal]
        for port, state in port_info.items():
            print("Port: %s \t State: %s" % (port,state))

