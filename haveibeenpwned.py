import requests 
from bs4 import BeautifulSoup
# have i been pwned

def live_checker(site):

    response = requests.get(site)
    return response.status_code







def pwn_checker(email):
    status_code = live_checker(website)
    sending_request = requests.get(website, cookies=cookie, headers=headers)
    print(sending_request)
    if status_code == 200:
        print("The Website is live.")
        print("Checking for the email {0}".format(email))
        # Now we are gonna post.

        sending_request = requests.get(website, cookies=cookie, headers=headers)
        print(sending_request)
        soup = BeautifulSoup(sending_request.content, 'html5lib')
        print(soup)
    else:
        print("The website seems Unreachable with status code {0} ".format(status_code))


website = "https://haveibeenpwned.com/unifiedsearch/dhakalabhishek128%40gmail.com"
cookie = {"__cf_bm":"zA6zzeV1Oj3GhX40r1NNhgJ5zSjz7mrA5mMYpiV6X.g-1717472643-1.0.1.1-Ii84rSjOFH0SPuTNzBnQvzRwhe7aO93QFUFNb2qrnuLFCmEloaI4FAkhLl5PWVk2OUb.akp4HmRKcrJRgmSkZw; perf_dv6Tr4n=1" }
headers = {"Cf-Turnstile-Response": "0.V8ldEVSPnOiubXrkZY_Uyo6yXKMgYuxXNWvAi01H89ffSX3Jk_XZk-7OYpplKicKy4oGQyKXxLTDhmj7HVvxK_lcau3Y4oTJ68Al9e5u71PoSpRVSTuW48J-ua_3wI8oZFcdIsND-FNrXLEDfqF3A23Ox3q3X2Ip6ywxSji76JdFS5MteYs7IXOBRT_Hv-Ne_sH1tWjBbpD8THFSJyOgj76UwLpW9lUJLS-lQ649SA-Y4c_vAsi5MQCU2dNo3QrjTYRPsQTlNgBAFOLHcSTmE_0S7C5CjGoso_ZjDTzgQ6HQHNnvAjoK5rnERjTI3TxvPYovs0JnS-qqmOi4A8vZfW2HO2T6pOzQ9c2hyi_QG6haiqzfzMBJFS57HnLZp3Na0yt8rwSXgWYe-1RpTRo1Rhkdpt7qMqWLL8RloSIpT358eG4y891UHNmccJ4KdRQB.MZm_g7iYaQten1SsSW7GYw.5030b3c43cc84be69c42d2263c91c78043318abf0c2e5b26e2dc9f92848f5320"}
# website = "https://haveibeenpwned.com/"
user_email = 'dhakalabhishek128@gmail.com'
pwn_checker(user_email)




# Cf_Turnstile_Response =  "0.1iB5UTd8YjnrfnP7GtEEf88fHQxNIN41c_2jJo4Ybo2RqWmosvY7jU_qMfHIW7FGXdvVfiLOhDBNGwPg9XpdAL49dGED3j4ZoqPFZc3n6bG_Zo9U5NnOwL5dP9UCY4QCAR_SEKQeEjdbVrmqmMa2m8VJEXGRd9OwK2KvuNVDd2Kgli1xE3FKXPy8an1nztweDWtuxCZEH6OF_eh_WUQMqycRS4grlaANIZSEJUJhv5tkUx-5aA_O94JAwybVXurgv6oOcnPBrWnsoJntlpCyiXXcWaq4mkADuFjbeoNuCXmkJ3rYMdjhC57cYhWvdv_CRuIzIM6lE5yG71pRwuUTEYUyLvhLeH56mAwq4nwS_C9vBOrOko2vFaztakjsM9vQUgXfYYRCTSxZKdX0Wj4yvrdrjOe1dEVq0MOyPRuHJjGAnbGWVGuOwJSx69258Fjx.hGNIrvUrRktFrulxdblciw.4086c3abb999a2c7c12975f19c855c4e148f47c93e25658f9dbdf7ed5ced47d6"






# THe site valdiates a token Cf_Turnstile_Response and everytime this token is new so not possible scraping this website.