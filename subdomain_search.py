from re import sub
import requests as req
from bs4 import BeautifulSoup
import os

url = 'https://crt.sh'
ends_with = ['.com', '.br', '.org', '.co', '.tv', '.dev', '.net']

def check_ends_with(website: str):
    for statement in ends_with:
        if website.endswith(statement):
            return True
            
def make_api_call(url, website):
    response = req.get(f'{url}/?q={website}')
    return response.text


def create_html_file(file_name, value):
    with open(file_name + '.html', "w", encoding="utf-8") as f:
        f.write(value)

def create_csv_file(file_name: str, subdomains: list[str]):
    open(file_name + '.csv', '+w')
    
    file = open(file_name + '.csv', '+a')
    for sub in subdomains:
        file.write(sub + ',')
    file.close()

def create_txt_file(file_name: str, subdomains: list[str]):
    open(file_name + '.txt', '+w')
    
    file = open(file_name + '.txt', '+a')
    for sub in subdomains:
        file.write(sub + '\n')
    file.close()

def extract_all_subdomains(res):
    soup = BeautifulSoup(res, 'html.parser')
    results = []
    subdomains = []
    
    all_table_rows = soup.find_all('tr')
    for table_data in all_table_rows:
        result = table_data.text.split('\n')  
        for item in result:
            line = item.split('\n')
            for sub in line:
                results.append(sub)
            
    for item in results:
        if check_ends_with(item):
            subdomains.append(item)
            
    return subdomains

def check_duplicates(subdomains):
    unitary_subs = []
    for sub in subdomains:
        if not unitary_subs.__contains__(sub):
            unitary_subs.append(sub)
        
    return unitary_subs

def show_all_subdomains(website):
    res = make_api_call(url, website)
    subdomains_with_duplicates = extract_all_subdomains(res)
    subdomains = check_duplicates(subdomains_with_duplicates)
    
    return subdomains


def create_all_files(website):
    res = make_api_call(url, website)
    subdomains_with_duplicates = extract_all_subdomains(res)
    subdomains = check_duplicates(subdomains_with_duplicates)

    
    create_csv_file('subdomains', subdomains)
    create_txt_file('subdomains', subdomains)
    

def delete_all_files():
    home_path = os.getcwd()
    files = os.listdir(home_path)

    for item in files:
        if item.endswith('.csv'):
            os.remove(home_path + '/' + item)
        if item.endswith('ins.txt'):
            os.remove(home_path + '/' + item)
