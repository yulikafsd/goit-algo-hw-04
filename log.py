from colorama import Fore

def log_dir(name):
    print(f"{Fore.BLUE} [DIR-] {Fore.RESET} {name}")

def log_file(name):
    print(f"{Fore.YELLOW} [FILE] {Fore.RESET} {name}")

def log_error(message):
    print(f"{Fore.RED} [ERROR] {Fore.RESET} {message}")