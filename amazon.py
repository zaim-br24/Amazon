from bs4 import BeautifulSoup
from time import sleep
import requests
import pandas as pd




website = "https://www.amazon.com/s?k=shoes&i=fashion-mens-intl-ship&crid=2AQQ0F5VA08X&sprefix=sh%2Cfashion-mens-intl-ship%2C442&ref=nb_sb_ss_ts-doa-p_1_2"

header = ({"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36","Accept-Language":"ar-MA,ar;q=0.9,en-US;q=0.8,en;q=0.7","Accept-Encoding":"gzip, deflate, br"})

r = requests.get(website, headers=header)


soup = BeautifulSoup(r.content, "html.parser")

pack = soup.find_all("div", {"class":"a-section a-spacing-base"})


name = []
price = []
real_price = []
delivery_price = []
rating = []
rating_count = []


for info in pack :

    name = []
    try :
        name.append(info.find("span", {"class":"a-size-base-plus a-color-base a-text-normal"}).text)
    except :
        print("n/a")

    price = []
    try :
        price.append(info.find("span", {"class":"a-offscreen"}).text)
    except :
        print("n/a")

    real_price = []
    try :
        real_price.append(info.find("span", {"class":"a-price a-text-price"}).text)
    except :
        print("n/a")
    
    delivery_price = []
    try :
        delivery_price.append(info.find("div", {"class":"a-row a-size-base a-color-secondary s-align-children-center"}).text)  
    except :
        print("n/a")

    rating = []
    try :
        rating.append(info.find("span", {"class":"a-icon-alt"}).text)
    except :
        print("n/a")
    
    rating_count = []
    try :
        rating_count.append(info.find("span", {"class":"a-size-base s-underline-text"}).text)
    except :
        print("n/a")

    print((name))
 
 


    













