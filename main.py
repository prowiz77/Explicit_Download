import re
import os
import sys
from colorama import Fore, Style

# supported for
#
# sexygirlspics.com
# pornpics.com
# nastypornpics.com
# gotanynudes.com

def check_push_folder():

    try:
        with open("push_folder.txt", "r") as file:
            content = file.read().strip()  
    except FileNotFoundError:
        content = ""

    
    if not content:
        
        target_folder = input(f"[{Fore.YELLOW}config{Style.RESET_ALL}] path to pushfolder {Fore.RED}>{Style.RESET_ALL} ")
        
        
        with open("push_folder.txt", "w") as file:
            file.write(target_folder)
    else:
        target_folder = content

    return target_folder

def create_downloads_folder():
    downloads_folder = "Downloads"
    if not os.path.exists(downloads_folder):
        os.mkdir(downloads_folder)
        print(f"[{Fore.YELLOW}config{Style.RESET_ALL}] -> {downloads_folder}")

    images_folder = os.path.join(downloads_folder, "Images")
    if not os.path.exists(images_folder):
        os.mkdir(images_folder)
        print(f"[{Fore.YELLOW}config{Style.RESET_ALL}] -> {images_folder}")

    videos_folder = os.path.join(downloads_folder, "Videos")
    if not os.path.exists(videos_folder):
        os.mkdir(videos_folder)
        print(f"[{Fore.YELLOW}config{Style.RESET_ALL}] -> {videos_folder}")

def get_user_folder_name():
    folder_name = input(f"[{Fore.BLUE}model-name{Style.RESET_ALL}] {Fore.RED}>{Style.RESET_ALL}")
    return folder_name

def menu():
    os.system('clear')
    print("")
    print("  _____                      _                 _           ")
    print(" |  __ \                    | |               | |          ")
    print(" | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ ")
    print(" | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
    print(" | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
    print(" |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ")
    print("")
    print("+----------------------------------------------------------+")
    print("|Please choose 1 or 2:                                     |")
    print("+----------------------------------------------------------+")
    print("| 1. Download Image                                        |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.sexygirlspics.com                     |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.pornpics.com                          |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.nastypornpics.com                     |")
    print("|                                                          |")
    print("| 2. Download Video                                        |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.gotanynudes.com                       |")
    print(f"|    [{Fore.RED}x{Style.RESET_ALL}] https://www.pornhub.com                           |")
    print("+----------------------------------------------------------+")
    print("| Push                                                     |")
    print("|     push. upload files to folder                         |")
    print("|     edit. edit/configure upload folder direcory          |")
    print("+----------------------------------------------------------+")

def main():
    menu()
    create_downloads_folder()
    check_push_folder()
    wahl = input(f"      {Fore.RED}>{Style.RESET_ALL} ")
    if wahl == "1":
        url = input(f"[{Fore.BLUE}url{Style.RESET_ALL}] {Fore.RED}> {Style.RESET_ALL}")

        if re.search(r'sexygirlspics\.com', url):
            folder_name = get_user_folder_name()
            os.system(f"python3 image_crawler.py {url} {folder_name}")
        elif re.search(r'pornpics\.com', url):
            folder_name = get_user_folder_name()
            os.system(f"python3 image_crawler.py {url} {folder_name}")
        elif re.search(r'nastypornpics\.com', url):
            folder_name = get_user_folder_name()
            os.system(f"python3 image_crawler.py {url} {folder_name}")
        else:
            print(f"[{Fore.RED}error{Style.RESET_ALL}] can't download url")

    elif wahl == "2":
        url = input(f"[{Fore.BLUE}url{Style.RESET_ALL}] {Fore.RED}> {Style.RESET_ALL}")

        if re.search(r'gotanynudes\.com', url):
            folder_name = get_user_folder_name()
            os.system(f"python3 video_crawler.py {url} {folder_name}")
        else:
            print(f"[{Fore.RED}error{Style.RESET_ALL}] can't download url")
    elif wahl == "push":
        os.system(f"python3 push.py")
    elif wahl == "edit":
        os.system(f"python3 edit_push.py")
    elif wahl == "exit":
        os.system('clear')
        exit()
    else:
        print(f"[{Fore.RED}Error{Style.RESET_ALL}] -> No valid option selected")

if __name__ == "__main__":
    main()