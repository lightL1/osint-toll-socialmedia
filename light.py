import requests
from colorama import init, Fore, Style
import pyfiglet
print('-----------------------------------------------------------------------------')
print(Fore.BLUE + "Oi tudo bom pessoal esse ´e meu  projeto pessoal pasiico  espero  cativar a todos")
print('-----------------------------------------------------------------------------')
print(Fore.BLUE + "eu espero  que possam deifar  seuas opinios aqui na git ajudaria muito")
print('-----------------------------------------------------------------------------')
print(Fore.RED + "import baner ...") 
print('-----------------------------------------------------------------------------')
init(autoreset=True)

def sherlock(username):
    sites = ["https://www.instagram.com/{}", "https://www.facebook.com/{}", "https://t.me/{}",
     "https://twitter.com/{}", "https://tryhackme.com/{}", "https://www.threads.net/{}",
     ]  # Adicione mais sites conforme necessário


    banner = pyfiglet.figlet_format("LIGHT_DEV")
    print(Fore.RED + banner)

    for site in sites:
        url = site.format(username)
        response = requests.get(url)
        
        if response.status_code == 200:
            print(Fore.GREEN + f"[+]Perfil encontrado: {url}")
        else:
            print(Fore.RED + f"[-]Perfil não encontrado em {url}")

username = input("digite_seu_username:")  # Substitua pelo nome de usuário que deseja pesquisar
sherlock(username)

