import ConfigParser
import os
import requests
import sys
import requests.packages.urllib3 as urllib3

from requests.auth import HTTPBasicAuth

def main():
    urllib3.disable_warnings()
    path, url = sys.argv[1:]
    with open(os.path.expanduser(path)) as auth_source:
        username, password = auth_source.read().strip().split(':')
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    if response.status_code != 200 or not response.text.startswith('<SUCCESS CODE="20'):
        print response.text

if __name__=='__main__':
    main()
