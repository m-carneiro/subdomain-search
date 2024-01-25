import requests as req
from bs4 import BeautifulSoup
import sys
import os

from model import Subdomains

url = 'https://crt.sh'
website = str(sys.argv[1])

ends_with = ['.com', '.br', '.org', '.co', '.tv', '.dev', '.net']

def check_ends_with(website):
    for statement in ends_with:
        if website.endswith(statement):
            return True
        return False
            
def make_api_call(url: str, website: str) -> str:
    response = req.get(f'{url}/?q={website}')
    return response.text

def create_html_file(file_name: str, value):
    file = open(file_name + '.html', '+a')
    file.write(value)

def create_csv_file(file_name: str, value: str):
    file = open(file_name + '.csv', '+a')
    file.write(value + ',')

    print('Created subdomains.csv on the directory')

def create_txt_file(file_name: str, value: str):
    file = open(file_name + '.txt', '+a')
    file.write(value + '\n')

    print('Created subdomains.txt on the directory')

def extract_html_files_for_testing(res: str):
    soup = BeautifulSoup(res, 'html.parser')
    subdomains = []
    
    all_table_rows = soup.find_all('tr')
    for table_data in all_table_rows:
        result = table_data.text.split('\n')
        if result.len() >= 6:
            subdomain = Subdomains(
                result[0].strip(),
                [
                    result[1].strip(),
                    result[2].strip(),
                    result[3].strip()
                ],
                [
                    result[4].strip(),
                    result[5].strip()
                ],
                result[6].strip()
            )
            subdomains.append(subdomain)

    return subdomains

def extract_all_subdomains(res: str) -> list[str]:
    soup = BeautifulSoup(res, 'html.parser')
    subdomains = []
    
    all_table_rows = soup.find_all('tr')
    for table_data in all_table_rows:
        result = table_data.text.split('\n')
        subdomain = Subdomains(
            result[0].strip(),
            [
                result[1].strip(),
                result[2].strip(),
                result[3].strip()
            ],
            [
                result[4].strip(),
                result[5].strip()
            ],
            result[6].strip()
        )
        subdomains.append(subdomain)

    return subdomains

def check_duplicates(subdomains: list[str]) -> list[str]:
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
file = extract_html_files_for_testing(res)
create_html_file('tables', file)

create_all_files()
