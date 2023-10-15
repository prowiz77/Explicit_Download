import os
import requests
import re
import sys
from colorama import Fore, Style


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

while True:
    if len(sys.argv) > 2:
        url = sys.argv[1]
        folder_name = sys.argv[2]

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
        os.system(f"python3 main.py")

    else:
        print(f"[{Fore.RED}error{Style.RESET_ALL}] Please provide a URL and folder name as arguments to run the video crawler.")
        os.system(f"python3 main.py")
