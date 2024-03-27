import requests
from bs4 import BeautifulSoup
from datetime import date

URL = "https://piter-lanch.ru/obedy/"
today = date.today().strftime("%d.%m.%Y")

def parse_html(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    return soup

def get_menu(soup, date=today):
    menu_items = [[] for i in range(4)]
    dates = {}
    
    dates_available = soup.find_all("div", class_="sel-sect__day-date")

    for each_date in dates_available:
        dates[each_date.text] = each_date.parent["href"][1:]
    
    if date in dates.keys():
        menu_link = dates[date]
    else:
        return "Date is not available"

    menu = soup.find(id=menu_link)
    items = menu.find_all("div", class_="sel-sect__items")

    for i in range(4):
        item = items[i].find_all("div", class_="sel-sect__item")
        for each_item in item:
            name = each_item.find("span", class_="sel-sect__item-title")
            image = "https://piter-lanch.ru" + each_item.find("img")["src"]
            text = each_item.find("div", class_="sel-sect__item-text")
            if text.text:
                menu_items[i].append([name.text, image, text.text])
            else:
                menu_items[i].append([name.text, image])
               
    return menu_items

print(get_menu(parse_html(URL)))