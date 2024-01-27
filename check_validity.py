from utils import show_better_messages, append_it
import time
import requests as req
import socket

subdomains = open("subdomains.txt").read().splitlines()
print("Checking subdomains...")
print('-' * 30)
time.sleep(1)

def check_starts_with(sub):
    if sub.startswith('*.'):
        return True
    return False
    
def make_api_call(subdomain):
    response = req.get(f'http://{subdomain}')
    return response

def is_reachable(ip_or_name, port, timeout=2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip_or_name, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

for sub in subdomains:
    if not check_starts_with(sub):
        if is_reachable(sub, 80):    
            is_ok = make_api_call(sub)
            message = show_better_messages(is_ok, sub)
            append_it(sub, message)

