import requests
from time import sleep



url = "https://www.google.com"
# url = "https://localhost:8080/"
url = "http://172.16.145.130/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "DNT": "1"
}


response = requests.get(url)
httpd_status_code = response.status_code
print(type(httpd_status_code))

def status_code():
    if httpd_status_code == 200:
        print("The website seems up")
        bruteforce()
    else: 
        print("Try another target.")



results = []  # A list woth words
def bruteforce():
    counter = 1
    words = open('small.txt', 'r')   #Opening the wordlist for reading
    try:
        for dir in words:
            url = "http://172.16.145.130/" + dir.strip()
            response = requests.get(url,headers=header)
            print(f"{counter}. {url}, status-code: {response.status_code},")
            counter = counter + 1 
            if counter % 1000 == 0:
                sleep(1)
            if response.status_code == 200:
                results.append(url)
    except ConnectionResetError as e:
         print("Facing issues but will continues",e)
         sleep(4)
    except requests.exceptions.ConnectionError as  e:
         print("Facing issues but will continues",e)
         sleep(4)
     
    finally:
        print("******************************")
        for i in results:
            print(f"{i} with status code 200/OK")


status_code()


