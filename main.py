import re
import os
import sys
from colorama import Fore, Style
import subprocess
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import shutil
import platform

# supported for
#
# sexygirlspics.com
# pornpics.com
# nastypornpics.com
# gotanynudes.com
# pornhub.com
# xhamster.com
#------------------------------------video_crawler----------------------------------------------------------------------------------------------------
def vid_crawler(url, folder_name):
    def extract_video_links(url):
        response = requests.get(url)
    
        if response.status_code == 200:
            page_content = response.text
            video_links = set()


            video_extensions = ['mp4', 'mov', 'mpeg', 'gif']
            pattern = r'(https?://[^\s/$.?#].[^\s]*)'
            for ext in video_extensions:
                pattern += f'\.{ext}|'
            pattern = pattern[:-1]  

            matches = re.finditer(pattern, page_content, re.IGNORECASE)
            for match in matches:
                video_links.add(match.group(0))

            return video_links

        return None
    
    def download_links_from_file(links_file, download_folder):
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        with open(links_file, "r") as file:
            for line in file:
                url = line.strip()
                if url:
                    os.system('clear')
                    print(f"[{Fore.YELLOW}url{Style.RESET_ALL}] -> {url}")
                    print(f"[{Fore.YELLOW}folder{Style.RESET_ALL}] -> {download_folder}")
                    download_file(url, download_folder)
    
    def download_file(url, folder):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
        
            content_length = response.headers.get('Content-Length')
            if content_length is not None:
                file_size = int(content_length)
                print(f"[{Fore.YELLOW}filesize{Style.RESET_ALL}] {file_size} Bytes")

            filename = os.path.join(folder, url.split("/")[-1])
            downloaded_bytes = 0  

            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        downloaded_bytes += len(chunk)

                        if file_size is not None:
                        
                            progress = (downloaded_bytes / file_size) * 100
                            print(f"[{Fore.YELLOW}Download{Style.RESET_ALL}] {Fore.YELLOW}{progress:.2f}%{Style.RESET_ALL}", end='\r')

    
    video_links = extract_video_links(url)

    if video_links:
        with open("links.txt", "w") as file:
            for link in video_links:
                file.write(link + '\n')
        print(f"{Fore.YELLOW}### {Style.RESET_ALL}{Fore.WHITE}[Progress] Video links saved to 'links.txt'{Style.RESET_ALL}{Fore.YELLOW} ###{Style.RESET_ALL}")

    links_file = "links.txt"  
        
    download_folder = os.path.join("Downloads","Videos", folder_name)
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    download_links_from_file(links_file, download_folder)
    print(f"[{Fore.GREEN}downloaded{Style.RESET_ALL}] -> {download_folder}")
    os.remove("links.txt")
#------------------------------------image_crawler_1----------------------------------------------------------------------------------------------------
def img_crawler_1(url):
    #url = input(f"[{Fore.BLUE}url{Style.RESET_ALL}] {Fore.RED}> {Style.RESET_ALL}")
    folder_name = get_user_folder_name()

    def download_file(url, folder):
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.join(folder, url.split("/")[-1])
            with open(filename, 'wb') as f:
                f.write(response.content)

    download_folder = os.path.join("Downloads","Images", folder_name)
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    response = requests.get(url)
    if response.status_code == 200:

        with open("img_links.txt", "w") as img_links_file:
            folder_path = download_folder


            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            soup = BeautifulSoup(response.text, 'html.parser')


            links = soup.find_all('a', href=True)

            for link in links:
                href = link['href']
                if re.search(r'\.(jpg|png|img|gif)', href, re.I):
                    img_links_file.write(href + '\n')

                    download_file(href, folder_path)

        print(f"[{Fore.GREEN}downloaded{Style.RESET_ALL}] -> {folder_path}")
        os.remove("img_links.txt")
    else:
        print(f"[{Fore.RED}error{Style.RESET_ALL}] Error retrieving the website.")
    #else:
        #print(f"[{Fore.RED}error{Style.RESET_ALL}] Please provide a URL and folder name as arguments to run the image crawler.")
#------------------------------------image_crawler_2----------------------------------------------------------------------------------------------------
def img_crawler_2(url, folder_name):
    def extract_video_links(url):
        response = requests.get(url)
    
        if response.status_code == 200:
            page_content = response.text
            video_links = set()


            video_extensions = ['jpg']
            pattern = r'(https?://[^\s/$.?#].[^\s]*)'
            for ext in video_extensions:
                pattern += f'\.{ext}|'
            pattern = pattern[:-1]  

            matches = re.finditer(pattern, page_content, re.IGNORECASE)
            for match in matches:
                video_links.add(match.group(0))

            return video_links

        return None

    def download_links_from_file(links_file, download_folder):
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        with open(links_file, "r") as file:
            for line in file:
                url = line.strip()
                if url:
                    os.system('clear')
                    print(f"[{Fore.YELLOW}url{Style.RESET_ALL}] -> {url}")
                    print(f"[{Fore.YELLOW}folder{Style.RESET_ALL}] -> {download_folder}")
                    download_file(url, download_folder)
    
    def download_file(url, folder):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
        
            content_length = response.headers.get('Content-Length')
            if content_length is not None:
                file_size = int(content_length)
                print(f"[{Fore.YELLOW}filesize{Style.RESET_ALL}] {file_size} Bytes")

            filename = os.path.join(folder, url.split("/")[-1])
            downloaded_bytes = 0  

            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        downloaded_bytes += len(chunk)

                        if file_size is not None:
                        
                            progress = (downloaded_bytes / file_size) * 100
                            print(f"[{Fore.YELLOW}Download{Style.RESET_ALL}] {Fore.YELLOW}{progress:.2f}%{Style.RESET_ALL}", end='\r')
    
    def delete_not_model(links_datei, name_model):
        with open(links_datei, 'r') as file:
            links = file.readlines() 

        präfixe = set()
        beste_links = []

        for link in links:
            link = link.strip()
            if not link:
                continue

            if name_model in link:
                präfix_match = re.search(r'(.+)-(\d+x\d+)\.jpg', link)
                if präfix_match:
                    präfix, auflösung = präfix_match.groups()
                    auflösung = tuple(map(int, auflösung.split('x')))
                    präfixe.add(präfix)
                    if not beste_links or auflösung > beste_links[1]:
                        beste_links = (link, auflösung)

        with open(links_datei, 'w') as file:
            for link in links:
                link = link.strip()
                if not link:
                    continue
                #####################s
                if name_model in link:
                    file.write(link + '\n')
    
    def delete_low_res(links_datei):
        with open(links_datei, 'r') as file:
            links = file.readlines()

        link_dict = {}  

        for link in links:
            link = link.strip()
            if not link:
                continue


            match = re.match(r'(.+)-(\d+x\d+)\.jpg', link)
            if match:
                name, auflösung = match.groups()
                auflösung = tuple(map(int, auflösung.split('x')))  


                if name in link_dict:
                    if auflösung > link_dict[name][0]:
                        link_dict[name] = (auflösung, link)
                else:
                    link_dict[name] = (auflösung, link)


        with open(links_datei, 'w') as file:
            for name, (auflösung, link) in link_dict.items():
                file.write(f"{link}\n")

    video_links = extract_video_links(url)

    if video_links:
        with open("links.txt", "w") as file:
            for link in video_links:
                file.write(link + '\n')
        print(f"{Fore.YELLOW}### {Style.RESET_ALL}{Fore.WHITE}[Progress] Video links saved to 'links.txt'{Style.RESET_ALL}{Fore.YELLOW} ###{Style.RESET_ALL}")

    links_file = "links.txt"  
        
    download_folder = os.path.join("Downloads","Images", folder_name)
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        

    delete_not_model(links_file, folder_name)
    delete_low_res(links_file)
    download_links_from_file(links_file, download_folder)
    print(f"[{Fore.GREEN}downloaded{Style.RESET_ALL}] -> {download_folder}")
    os.remove("links.txt")
#------------------------------------xhamster_Download----------------------------------------------------------------------------------------------------
def find_and_save_mp4_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        mp4_pattern = re.compile(r'https?://.*\.mp4')
        with open('mp4_links.txt', 'w') as mp4_file:
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and mp4_pattern.search(href):
                    mp4_url = urljoin(url, href)  
                    mp4_file.write(mp4_url + '\n')
        
        print(f"[{Fore.YELLOW}process{Style.RESET_ALL}] -> .mp4-link saved to 'mp4_links.txt'")
    
    except Exception as e:
        print(f'[{Fore.RED}error{Style.RESET_ALL}] Error occured while downloading or analyying element {e}')

def download_hamster():
    def get_user_folder_name():
        folder_name = input(f"[{Fore.BLUE}model-name{Style.RESET_ALL}] {Fore.RED}> {Style.RESET_ALL}")
        return folder_name

    def download_mp4_files(links, download_directory):
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
    
        for link in links:
            try:
                response = requests.get(link)
                response.raise_for_status()
                file_name = link.split("/")[-1]
                file_path = os.path.join(download_directory, file_name)
                with open(file_path, 'wb') as mp4_file:
                    mp4_file.write(response.content)
            
                print(f'[{Fore.GREEN}downloaded{Style.RESET_ALL}] -> file stored in {download_directory}')
        
            except Exception as e:
                print(f'[{Fore.RED}error{Style.RESET_ALL}] Error while downloading file {e}')

    folder_name = get_user_folder_name()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    download_directory = os.path.join(script_directory, 'Downloads', 'Videos', folder_name) 
    with open('mp4_links.txt', 'r') as file:
        mp4_links = file.read().splitlines()

    download_mp4_files(mp4_links, download_directory)
    os.remove("mp4_links.txt")
#------------------------------------push_function----------------------------------------------------------------------------------------------------
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
#------------------------------------real_push_function----------------------------------------------------------------------------------------------------
def real_push_function():
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
#------------------------------------edit_push_function----------------------------------------------------------------------------------------------------
def edit_push_function():
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
#------------------------------------create_Download_folder----------------------------------------------------------------------------------------------------
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
#------------------------------------folder_name_function----------------------------------------------------------------------------------------------------
def get_user_folder_name():
    folder_name = input(f"[{Fore.BLUE}model-name{Style.RESET_ALL}] {Fore.RED}> {Style.RESET_ALL}")
    return folder_name
#------------------------------------pornhub_download----------------------------------------------------------------------------------------------------
def youtube_dl():
    folder_name = get_user_folder_name()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    target_folder = os.path.join(script_directory, 'Downloads', 'Videos', folder_name) 
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)
    os.chdir(target_folder)
#------------------------------------menu_function----------------------------------------------------------------------------------------------------
def menu():
    os.system('clear')
    print(f"{Fore.MAGENTA}")
    print("  _____                      _                 _           ")
    print(" |  __ \                    | |               | |          ")
    print(" | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ ")
    print(" | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
    print(" | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
    print(" |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ")
    print(f"{Style.RESET_ALL}")
    print("+----------------------------------------------------------+")
    print(f"|Please choose {Fore.RED}1{Style.RESET_ALL} or {Fore.RED}2{Style.RESET_ALL} or {Fore.RED}push{Style.RESET_ALL} or {Fore.RED}edit{Style.RESET_ALL}:                     |")
    print("+----------------------------------------------------------+")
    print(f"| {Fore.CYAN}1{Style.RESET_ALL}. Download Image                                        |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.sexygirlspics.com                     |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.pornpics.com                          |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.nastypornpics.com                     |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.gotanynudes.com                       |")
    print("|                                                          |")
    print(f"| {Fore.CYAN}2{Style.RESET_ALL}. Download Video                                        |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.gotanynudes.com                       |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.pornhub.com                           |")
    print(f"|    [{Fore.GREEN}x{Style.RESET_ALL}] https://www.xhamster.com                          |")
    #print("+----------------------------------------------------------+")
    print("|                                                          |")
    print("| Push                                                     |")
    print(f"|     {Fore.CYAN}push{Style.RESET_ALL}. upload files to folder                         |")
    print(f"|     {Fore.CYAN}edit{Style.RESET_ALL}. edit/configure upload folder direcory          |")
    print("+----------------------------------------------------------+")
    print(f"| {Fore.YELLOW}!Attention!{Style.RESET_ALL}                                              |")
    print(f"|    [{Fore.YELLOW}!{Style.RESET_ALL}]{Fore.YELLOW} use a vpn for downloading{Style.RESET_ALL}                         |")
    print(f"|    [{Fore.YELLOW}!{Style.RESET_ALL}]{Fore.YELLOW} slow download speeds for https://www.xhamster.com{Style.RESET_ALL} |")
    print("+----------------------------------------------------------+")

#------------------------------------main_function----------------------------------------------------------------------------------------------------
def main():
    os.system('clear')
    menu()
    create_downloads_folder()
    check_push_folder()
    wahl = input(f"      {Fore.RED}>{Style.RESET_ALL} ")
    if wahl == "1":
        url = input(f"[{Fore.BLUE}url{Style.RESET_ALL}] {Fore.RED}> {Style.RESET_ALL}")

        if re.search(r'sexygirlspics\.com', url):
            img_crawler_1(url)
        elif re.search(r'pornpics\.com', url):
            img_crawler_1(url)
        elif re.search(r'nastypornpics\.com', url):
            img_crawler_1(url)
        elif re.search(r'gotanynudes\.com', url):
            folder_name = get_user_folder_name()
            img_crawler_2(url, folder_name)
        else:
            print(f"[{Fore.RED}error{Style.RESET_ALL}] can't download url")

    elif wahl == "2":
        url = input(f"[{Fore.BLUE}url{Style.RESET_ALL}] {Fore.RED}> {Style.RESET_ALL}")

        if re.search(r'gotanynudes\.com', url):
            folder_name = get_user_folder_name()
            vid_crawler(url, folder_name)
        elif re.search(r'pornhub\.com', url):
            folder_name = get_user_folder_name()
            script_directory = os.path.dirname(os.path.abspath(__file__))
            target_folder = os.path.join(script_directory, 'Downloads', 'Videos', folder_name) 
            if not os.path.exists(target_folder):
                os.mkdir(target_folder)
            os.chdir(target_folder)
            os.system(f"youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' {url}")
        elif re.search(r'xhamster\.com', url):
            find_and_save_mp4_links(url)
            download_hamster()
                   
        else:
            print(f"[{Fore.RED}error{Style.RESET_ALL}] can't download url")
    elif wahl == "push":
        real_push_function()
    elif wahl == "edit":
        edit_push_function()
    elif wahl == "exit":
        os.system('clear')
        exit()
    else:
        print(f"[{Fore.RED}Error{Style.RESET_ALL}] -> No valid option selected")

if __name__ == "__main__":
    main()
