import requests as req
from bs4 import BeautifulSoup
import sys
import os

url = 'https://crt.sh'
website = str(sys.argv[1])

ends_with = ['.com', '.br', '.org', '.co', '.tv', '.dev', '.net']

def check_ends_with(website):
    for statement in ends_with:
        if not website.endswith(statement):
            return False
        return True
            
def make_api_call(url, website):
    response = req.get(f'{url}/?q={website}')
    return response.text

def create_csv_file(file_name, value):
    file = open(file_name + '.csv', '+a')
    file.write(value + ',')

def create_txt_file(file_name, value):
    file = open(file_name + '.txt', '+a')
    file.write(value + '\n')

def extract_all_subdomains(res):
    soup = BeautifulSoup(res, 'html.parser')
    subdomain = []

    all_table_rows = soup.find_all('tr')
    for table_data in all_table_rows:
        result = table_data.text.split('\n')
        for item in result:
            print(item)
            if check_ends_with(item):
                subdomain.append(item)

    return subdomain

def check_duplicates(subdomains):
    unitary_subs = []
    for sub in subdomains:
        if not unitary_subs.__contains__(sub):
            unitary_subs.append(sub)
        
    return unitary_subs


def create_all_files():
    res = make_api_call(url, website)
    subdomains_with_duplicates = extract_all_subdomains(res)
    subdomains = check_duplicates(subdomains_with_duplicates)

    for sub in subdomains:
        create_csv_file('subdomains', sub)
        create_txt_file('subdomains', sub)
    

home_path = os.getcwd()
files = os.listdir(home_path)

for item in files:
    if item.endswith('subdomains.csv') or item.endswith('ins.txt'):
        os.remove(home_path + '/' + item)

res = make_api_call(url, website)
print(extract_all_subdomains(res))

# create_all_files()
