# coding:utf-8
import requests
import hashlib
import urllib
import re
from bs4 import BeautifulSoup

BASE_URL = 'https://fangj.github.io/friends/'
SCRIPT_FOLD = 'script/'

def crawl_script(episode_link, csv_file):
    response = urllib.request.urlopen(episode_link)  
    html = response.read()
    soup = BeautifulSoup(html, from_encoding='utf-8')
    dialog_list = soup.find_all('p')
    with open(csv_file, 'w') as f:
        for dialog in dialog_list:
            if dialog.b or dialog.strong:             
                try:
                    _str = str(dialog.text.encode('utf-8'))
                    role = _str.split(':')[0]
                    line = _str.split(':')[1]
                    f.write(str(role)[2:] + '\t' + str(line))
                    f.write('\n')
                except:
                    f.write('\n')


def crawl():
    '''
    get link for each episode
    '''
    response = urllib.request.urlopen(BASE_URL)  
    html = response.read()
    soup = BeautifulSoup(html, from_encoding='utf-8')
    episode_list = soup.find_all('a')
    for episode in episode_list:
        csv_file = SCRIPT_FOLD + episode.text.strip() + '.csv'
        # print(csv_file)
        # print(BASE_URL + episode['href'])
        crawl_script(BASE_URL + episode['href'], csv_file)

if __name__ == '__main__':
    crawl()