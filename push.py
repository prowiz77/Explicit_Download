import os
import shutil
import sys
import subprocess
import platform
from colorama import Fore, Style

def copy_files_to_target_folder():
    with open("push_folder.txt", "r") as file:
        target_folder = file.read().strip()  


    if os.path.exists(target_folder):
        shutil.rmtree(target_folder)

    downloads_folder = "Downloads"

    print(f"[{Fore.YELLOW}push{Style.RESET_ALL}] ...")

    shutil.copytree(downloads_folder, target_folder)

    print(f"[{Fore.YELLOW}push{Style.RESET_ALL}][{Fore.GREEN}successful{Style.RESET_ALL}] -> {target_folder}")

def tree_unix_only():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':

        with open("push_folder.txt", "r") as file:
            target_folder = file.read().strip()  
        

        tree_output = subprocess.check_output(["tree", target_folder])


        print(tree_output.decode("utf-8"))


copy_files_to_target_folder()
tree_unix_only()
os.system(f"python3 main.py")
