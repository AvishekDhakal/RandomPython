import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "close",
    "DNT": "1"
}
url = "https://thehackernews.com/search/label/Cyber%20Attack"
response = requests.get(url, headers=header)
httpd_status = response.status_code



def news_preview():
    if httpd_status == 200:
        soup = BeautifulSoup(response.content, 'html5lib')
        news_titles_tags = soup.find_all(class_= 'home-title')
        description = [a.text for a in soup.find_all(class_= "home-desc")]
        titles_only = [a.text for a in news_titles_tags]
        href_links = [a['href'] for a in soup.find_all(class_ ="story-link" )]


        for i in range(0,len(titles_only)):
            print(f"{i+1}. {titles_only[i]}",end="\n")
            print("")
            print("",end="\n")
            print(f"{description[i]}",end="\n")
            print("")
            print("",end="\n")
    return(href_links)
    

    
def full_news():
    try:
        news_links = news_preview()
        print(len(news_links))
        continue_prompt = str(input("---->Would you like to read any of the news complete?(y/n): "))
        if continue_prompt.lower()== 'y' or continue_prompt.lower() == 'yes':
            news_number = int(input(f"---->Give me the number in correspondance to news(1-{len(news_links)}): ")) #make this acccept only non negative.
            
            if news_number <= len(news_links) and news_number> 0:
                counter = 1
                if (news_number) <= len(news_links):

                    print(f"\nREQUESTING FOR THE NEWS: {news_links[news_number-1]}\n")
                    response_news = requests.get(news_links[news_number-1], headers=header)
                    if response_news.status_code == 200:
                        soup_content = BeautifulSoup(response_news.content,'html5lib')
                        news_story_title = soup_content.find(class_="story-title")
                        print(f"\t\t\t\t\t\t\t{news_story_title.text}\n\n")
                        news_story_body = soup_content.find_all(class_="articlebody clear cf")
                        for tags in news_story_body:
                            print((tags.text))
                    else:
                        print("Could no reach the page. Check internet.")
            else:
                print("No news for that number.")
        else:
            print("Bye Bye")
    except requests.exceptions.ChunkedEncodingError as e:
        print(f"Got some error.{e}")

full_news()