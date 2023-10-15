import requests
from bs4 import BeautifulSoup
import re
import os
import sys
from colorama import Fore, Style


def download_file(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(folder, url.split("/")[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        folder_name = sys.argv[2]

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
            os.system(f"python3 main.py")
        else:
            print(f"[{Fore.RED}error{Style.RESET_ALL}] Error retrieving the website.")
            os.system(f"python3 main.py")
    else:
        print(f"[{Fore.RED}error{Style.RESET_ALL}] Please provide a URL and folder name as arguments to run the image crawler.")
        os.system(f"python3 main.py")
