# -*- encoding=utf8 -*-
from requests import post
import requests
import re

def getContent(url):
    r = requests.get(url)
    return r.content

def getverifyRand(url):
    content = getContent(url)
    pattern = re.compile('.*?<input type="hidden" name="verifyRand" id="verifyRand" value="(.*?)"/>.*?')
    match = re.findall(pattern, content)
    verifyRand = match[0]
    return verifyRand

url_login = 'http://project.ct108.org/zentao/user-login.html'
url = 'http://project.ct108.org/zentao/bug-browse-480--byModule-5692.html'

data = {
    "account":"lujh",
    "password":"7734ae95a2d208ddc26f898787aee52c",
    "verifyRand":getverifyRand(url_login),
    }

cookie = post(url, data=data).cookies

print(cookie)