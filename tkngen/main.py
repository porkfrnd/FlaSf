import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser, re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

os.system("title [CMTL] GET EZZ")


def Spinner():
    l = ['|', '/', '-', '\\']
    for i in l + l + l:
        sys.stdout.write('\r' + Fore.YELLOW + 'Starting DiegoBotGen...' + i)
        sys.stdout.flush()
        time.sleep(0.2)


Spinner()

banner = (
            Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]\n" +
            Fore.WHITE + Fore.BLUE + '''\n  
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |      __      | || |  ________    | || |     _____    | || |  _________   | || |  ____  ____  | || |      __      | |
| |     /  \     | || | |_   ___ `.  | || |    |_   _|   | || | |  _   _  |  | || | |_  _||_  _| | || |     /  \     | |
| |    / /\ \    | || |   | |   `. \ | || |      | |     | || | |_/ | | \_|  | || |   \ \  / /   | || |    / /\ \    | |
| |   / ____ \   | || |   | |    | | | || |      | |     | || |     | |      | || |    \ \/ /    | || |   / ____ \   | |
| | _/ /    \ \_ | || |  _| |___.' / | || |     _| |_    | || |    _| |_     | || |    _|  |_    | || | _/ /    \ \_ | |
| ||____|  |____|| || | |________.'  | || |    |_____|   | || |   |_____|    | || |   |______|   | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' \n\n''' + Fore.RESET + Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]\n")

os.system("cls")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))

print(
    Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
print(
    Fore.WHITE + Fore.BLUE + "                                         Welcome to " + Fore.WHITE + " DiegoBot-Gen " + Fore.WHITE + "- 2021 -")
print(
    Fore.WHITE + Fore.BLUE + "                                         [1] " + Fore.WHITE + "Token Generator(super fast!)")
print(
    Fore.WHITE + Fore.BLUE + "                                         [2] " + Fore.WHITE + "Token Checker(Checks all tokens you generated)")
print(Fore.WHITE + Fore.BLUE + "                                         [3] " + Fore.WHITE + "Credits")
print(Fore.WHITE + Fore.BLUE + "                                         [4] " + Fore.WHITE + "Exit")
print(
    Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
opcion = input("\nChoice: ")
if opcion == '1':
    os.system("cls")
    print(banner)
    cantidad = input("\nAmount to generate: ")
    while int(count) < int(cantidad):
        Generated = "NT" + random.choice(string.ascii_letters) + ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(21)) + "." + random.choice(
            string.ascii_letters).upper() + ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(27))
        f = open(current_path + "/" + str("Generated") + str("") + ".txt", "a")
        f.write(Generated + "\n")
        print(Fore.GREEN + "Token: " + Fore.RESET + Generated)
        count += 1
        if int(count) == int(cantidad):
            print("\n" + Fore.CYAN + Fore.BLUE + "Tokens generated successfully!")
            print(Fore.WHITE + Fore.BLUE + "Tokens saved in Generated.txt")
            input(Fore.BLUE + Fore.BLUE + "\nPress enter to exit")
            os.system("cls")
            print(
                Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
            print(Fore.BLUE + Fore.BLUE + "                                                   Closing!")
            print(Fore.GREEN + Fore.BLUE + "                                               Have a good day :D")
            print(
                Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
            time.sleep(2)
            sys.exit()
            pass
    pass
if opcion == '2':
    os.system("cls")
    print("\n" + banner + "\n")
    with open('Generated.txt', 'r') as f:
        for line in f:
            time.sleep(0)
            token = line.rstrip("\n")
            headers = {
                'Authorization': f'{token}'
            }
            src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

            try:
                if src.status_code == 200:
                    print(f'{Fore.BLUE}InValid token! >{Fore.RESET} ' + token)
                else:
                    print(f'{Fore.LIGHTGREEN_EX}Valid token >{Fore.RESET} ' + token)
            except Exception:
                print(f"{Fore.CYAN}Error, please contact with DiegoBot#1739 {Fore.RESET}")
pass
if opcion == '3':
    os.system("cls")
    print(
        Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
    print(
        Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
    input(Fore.BLUE + Fore.BLUE + "\nEnter to exit")
    os.system("cls")
    print(
        Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
    print(Fore.BLUE + Fore.BLUE + "                                                   Closing!")
    print(Fore.GREEN + Fore.BLUE + "                                               Have a good day :D")
    print(
        Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
    time.sleep(2)
    sys.exit()
    pass
if opcion == '4':
    os.system("cls")
    print(
        Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
    print(Fore.BLUE + Fore.BLUE + "                                                   Closing!")
    print(Fore.GREEN + Fore.BLUE + "                                               Have a good day :D")
    print(
        Fore.WHITE + Fore.BLUE + "                         [" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]" + Fore.WHITE + Fore.BLUE + "-------------------------------------------------------" + Fore.WHITE + Fore.BLUE + "[" + Fore.WHITE + Fore.BLUE + "+" + Fore.WHITE + Fore.BLUE + "]")
    time.sleep(2)
    sys.exit()
    pass

