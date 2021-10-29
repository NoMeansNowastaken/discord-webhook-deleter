from colorama.ansi import Fore
import requests

url = input('Enter Url: ')
if 'https://discord.com/api/webhooks' in url:
    requests.delete(url=url)
    r = requests.get(url=url)
    if r.status_code == 404:
        print(f'{Fore.LIGHTGREEN_EX}Success{Fore.RESET}')
    else:
        print(f'{Fore.RED}Error{Fore.RESET}')
else:
    print(f'{Fore.RED}Invalid Url{Fore.RESET}')