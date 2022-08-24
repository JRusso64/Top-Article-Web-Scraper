from flask import Blueprint, render_template
import requests
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree

def techCrunch():
    url = "https://techcrunch.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    first = soup.find('a', {"class": "post-block__title__link"})
    return first['href']
    

def gizmodo():
    url = "https://gizmodo.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    found = False
    found2 = False
    count = 0

    for a in soup.find_all('a', href=True):
        if('/search' in a['href'] and found == True):
            found2 = True
        if('/search' in a['href'] and found == False):
            found = True
        
        if(found == True and found2 == True):
            found = soup.find_all('a', href=True)[count + 1]['href']
            return found
        count = count + 1
        
# def engadget():
#     url = "https://www.engadget.com/"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     temp = etree.HTML(str(soup))

#     result = temp.xpath('/html/body/div[1]/div[2]/div[2]/div/main/div[1]/div/section/div/div[2]/div[2]/div[1]/div[3]/article/div/div[2]/div/div/h2/a/@href')
#     # return "https://www.engadget.com" + result
#     return result

views = Blueprint('views', __name__)

data = [techCrunch(), gizmodo()]

@views.route('/')
def home():
    return render_template('base.html', data = data)