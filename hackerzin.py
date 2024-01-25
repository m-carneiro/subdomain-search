import sys
import os
from subdomain_search import show_all_subdomains

def main():        
    s = f"""
    {'-'*40}
    Hackerzin.py - A tool to find subdomains and it's things
    {'-'*40}
    Just so I can learn python and stuff
    And so I can make my life easier when I need to recon something
    @Author: @m-carneiro
    {'-'*40}
    """
    if sys.argv[1] == '-s' or sys.argv[1] == '--subdomain':     
        print(s)
        website = str(sys.argv[2])
        if website == "":
            print('You need to specify a website after the flag -s or --subdomain')
            sys.exit(1)
        
        if website.startswith('http://'):
            website = website.replace('http://', '')
            sub_list = show_all_subdomains(website)
            for sub in sub_list:
                print('& ->' + sub)
            
        sub_list = show_all_subdomains(website)
        for sub in sub_list:
            print('& ->  ' + sub)    
    
    if sys.argv[1] == '-v' or sys.argv[1] == '--version':
        print('Version: 0.0.1')
        sys.exit(1)

    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print(s)
        print('Usage: python3 hackerzin.py <website> <file_name> <file_extension>')
        print('Example: python3 hackerzin.py google.com google csv')
        sys.exit(1)

    if len(sys.argv) < 2:
        print(s)
        print('Use -h or --help to see the usage \n')
        print('If you just want to see subdomains use command below: \n')
        print('Usage: python3 hackerzin.py <website> \n')
        sys.exit(1)
        
main()

