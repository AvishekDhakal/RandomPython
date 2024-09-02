import requests

url = "https://thehackernews.com/search/label/Cyber%20Attack"

response = requests.Request('Get',url)
prepared_requests = response.prepare()

for key, value in prepared_requests.headers.items():
    print(f"{key}: {value}")
print(type(response))

response = requests.Response()
print(type(response))


# so what we have is 2 data type on is request and another is reposponse.

# the when you do requests.get(url) it throws the <class 'requests.models.Response'> as output and it have defied methods of how you can we them.




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive"
}


response = requests.get(url, headers=headers)
http_status = (response.status_code) 


#ok so when we do this and when we use response.text we are basically acessing thing like in list using indexing but rather here the value is what we provide and according to that value we get the reuslts.





if http_status == 200:
    print("Its running.")

for key, value in response.headers.items():
    print(f"{key}: {value}")

