import os
import shutil
import sys
from colorama import Fore, Style

def edit_push_folder():
    with open("push_folder.txt", "r") as file:
        current_target_folder = file.read().strip()

    print(f"[{Fore.YELLOW}currentdir{Style.RESET_ALL}] -> {current_target_folder}")

    new_target_folder = input(f"[{Fore.BLUE}new{Style.RESET_ALL}] {Fore.RED}>{Style.RESET_ALL} ").strip()

    if new_target_folder:
        with open("push_folder.txt", "w") as file:
            file.write(new_target_folder)
            print(f"[{Fore.YELLOW}currentdir{Style.RESET_ALL}] -> {new_target_folder} ")
    else:
        print(f"[{Fore.RED}!{Style.RESET_ALL}] no changes were made")

edit_push_folder()
os.system(f"python3 main.py")
