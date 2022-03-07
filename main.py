import os
import colorama
from colorama import Fore

colorama.init()

os.system("cls")
os.system('title [Beta] FlaSLF || Made by CatNomy')

print(f"""
{Fore.BLUE}
███████╗██╗      █████╗ ███████╗███████╗ |   |  ██████╗ ███████╗████████╗    ███████╗███████╗███████╗███████╗
██╔════╝██║     ██╔══██╗██╔════╝██╔════╝ |   | ██╔════╝ ██╔════╝╚══██╔══╝    ██╔════╝╚══███╔╝╚══███╔╝╚══███╔╝
█████╗  ██║     ███████║███████╗█████╗   |   | ██║  ███╗█████╗     ██║       █████╗    ███╔╝   ███╔╝   ███╔╝{Fore.BLUE} 
██╔══╝  ██║     ██╔══██║╚════██║██╔══╝   |   | ██║   ██║██╔══╝     ██║       ██╔══╝   ███╔╝   ███╔╝   ███╔╝  
██║     ███████╗██║  ██║███████║██║      |   |  ╚██████╔╝███████╗   ██║       ███████╗███████╗███████╗███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝      |   |   ╚═════╝ ╚══════╝   ╚═╝       ╚══════╝╚══════╝╚══════╝╚══════╝
{Fore.RED}
1. Discord Bot{Fore.BLUE}
2. Bot Nuker{Fore.RED}
3. Token gen {Fore.BLUE}       
4. SelfBot  {Fore.RED}
5. Ip lookup {Fore.BLUE}
6. Pinger {Fore.RED}                                                           
""")
print(Fore.RESET)
choice = input(f'{Fore.BLUE}Spit ur option out [>')
os.system('cls')

# relatables

if choice in ("1", "Discord Bot", "discord bot"):
    os.system('py ./bot/main.py')
if choice in ("2", "Bot Nuker", "bot nuker"):
    os.system('py ')
if choice in ("5", "ip lookup", "Ip Lookup"):
    os.system('py ./iplookup/ipmap.py')
if choice in ("6", "ip lookup", "Ip Lookup"):
    pinger_ip = input("The ip >")
    pinger_port = input("The port >")
    os.system("cd pinger")
    os.system("powershell")
    os.system(f"./main.py {pinger_ip} {pinger_port}")
    os.system(f"nslookup {pinger_ip}")
    os.system(f"ping {pinger_ip}")
    os.system("cd ../")
os.system('pause')
