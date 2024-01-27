

def show_better_messages(response, subdomain):
    if response.status_code == 200:
        return f'{subdomain} is valid!'
    elif response.status_code == 404:
        return f'{subdomain} is not valid!'
    elif response.status_code == 403:
        return f'{subdomain} is valid, but forbidden!'
    elif response.status_code == 400:
        return f'{subdomain} is valid, but bad request!'
    elif response.status_code == 500:
        return f'{subdomain} is valid, but internal server error!'
    elif response.status_code == 502:
        return f'{subdomain} is valid, but bad gateway!'
    elif response.status_code == 503:
        return f'{subdomain} is valid, but service unavailable!'
    elif response.status_code == 504:
        return f'{subdomain} is valid, but gateway timeout!'
    else:
        return f'{subdomain} is valid, but unknown error!'

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
    
def append_it(subdomain: str, value: str):
    file = open('subdomains.txt', 'r')
    lines = file.readlines()
    file.close()
    
    file = open('subdomains.txt', '+a')
    file.write('\n')
    file.write('\n')
    file.write('----------------- Checking Validity -----------------')
    file.write('\n')
    for line in lines:
        if line.strip() == subdomain:
            file.write(line.strip() + ' is reachable' + '\n')   #check if it's reachable
            file.write(line.strip() + value + '\n')             #check if it has a valid response
    file.close()
