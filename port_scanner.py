import socket
import subprocess
from uu import Error

import nmap

subdomains = open("subdomains.txt").read().splitlines()
ports = range(1, 65353)

def check_ends_with(subdomain: str):
    if subdomain.endswith('reachable'):
        return True
    return False

def get_ports_on_a_domain(domain: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((domain, port))
        return True
    except:
        return False
    
def use_nmap_instead():
    nmScan = nmap.PortScanner()
    for host in subdomains:
        print('Host : %s (%s)' % (host, nmScan[host].hostname()))
        print('State : %s' % nmScan[host].state())
        for proto in nmScan[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
        
            lport = nmScan[host][proto].keys()
            lport.sort()
            for port in lport:
                print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))

# for domain in subdomains:
#     print(f'Scanning {domain}...')
#     for port in ports:
#         if get_ports_on_a_domain(domain, port):
#             print(f'{domain} has port {port} open.')
#     print('-' * 30)
#     print(f'Finished scanning {domain}')


use_nmap_instead()