import os
import colorama
from colorama import Fore, Style

colorama.init()

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
1. Discord Bot
2. Bot Nuker
3. Token gen        
                                                                              
""")
print(Fore.RESET)
choice = input(f'{Fore.BLUE}Spit ur option out [>')
os.system('cls')

# relatables

if choice in ("1", "Discord Bot", "discord bot"):
    os.system('py ./bot/main.py')
if choice in ("2", "Bot Nuker", "bot nuker"):
    os.system('py ')

os.system('pause')
