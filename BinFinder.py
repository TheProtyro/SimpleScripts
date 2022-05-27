from bs4 import BeautifulSoup
import requests
import argparse

class color:
   CYAN = '\033[0;36;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[0;33;48m'
   END = '\033[1;37;0m'

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File with binary to test on GTFObins", type=str, required=True)
args = parser.parse_args()

bin_file = args.file

url = "https://gtfobins.github.io/gtfobins/"

print(color.YELLOW + "[+] Searching for binary on GTFObins:" + color.END, url)

with open(bin_file, 'r') as file:
    for bin in file:
        full_url_bin = url + bin[:-1]
        r = requests.get(full_url_bin)
        if r.status_code == 200:
            print(color.GREEN + '[+] Binary found: ' + bin[:-1] + ' ' + color.END, end='')
            soup = BeautifulSoup(r.text, 'html.parser')
            for tag in soup.find_all('h2'):
                    print(color.CYAN + '[ ' + tag['id'] + ' ]' + color.END, end ='')
            print('\r')
