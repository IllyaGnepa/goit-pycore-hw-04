import sys
from colorama import Fore
from pathlib import Path

def print_tree(path, prefix=''):
    for item in path.iterdir():
        if item.is_dir():
            print(f'{prefix}{Fore.GREEN}├── {item.name}{Fore.RESET}')
        else:
            print(f'{prefix}{Fore.BLUE}├── {item.name}{Fore.RESET}')
        if item.is_dir():
            print_tree(item, prefix + Fore.GREEN + '│   ' + Fore.RESET)
try:
    if Path(sys.argv[1]).exists()  == False:
        print("Path doen't exist")
    elif Path(sys.argv[1]).is_dir() == False:
        print("Please provide a directory")
    else:
        print(f"{Fore.RED}{Path(sys.argv[1])}{Fore.RESET}")
        print_tree(Path(sys.argv[1]))
except IndexError:
    print(("Empty input, please provide a directory"))

