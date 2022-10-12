import requests
from bs4 import BeautifulSoup
  
  
def horoscope( day,zodiac_sign):
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content,
                         "html.parser")
  
    return soup.find("div", class_="main-horoscope").p.text
  