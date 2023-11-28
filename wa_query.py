import urllib.parse
from bs4 import BeautifulSoup
import requests
import lxml

APP_ID = 'Q397JV-XU486TAYQX'

wa_preamble = 'http://api.wolframalpha.com/v2/query?appid=' + APP_ID + '&input='
wa_postamble = "&podstate=Step-by-step%20solution&format=image"

def conv_str(input_string) :
    return urllib.parse.quote(input_string)

def form_query(input) :
    return wa_preamble + conv_str(input) + wa_postamble

def get_imgs(query) :
    url = form_query(query)
    images = []

    response = requests.get(url)
    soup = BeautifulSoup(response.content, features = 'xml')

    for img in soup.findAll('img'):
        src = img.get("src")
        print(src)
        if src:
            images.append(src)
    return images