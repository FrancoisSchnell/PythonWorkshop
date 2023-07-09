from bs4 import BeautifulSoup
import requests

# Goal : searching news articles on ccn.unistra.fr

url = "https://ccn.unistra.fr/"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")
news = soup.find_all("div", class_="news-content")

for new in news:
    title = new.find("h3").text.strip()
    content = new.find("p").text.strip()
    print(f"{title} \n{content}\n")

if 0: 
    # or by using select: soup.select('.news-content p')
    ps= soup.select('.news-content p')
    ts= soup.select(".news-content h3")
    for i in range(len(ps)):
        print(ts[i].text.strip())
        print(ps[i].text.strip())