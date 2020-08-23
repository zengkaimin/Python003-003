#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 3:37 下午
# @Author  : Kaimin Zeng
# @File    : maoyan_by_requests_bs4.py

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
header = {'user-agent':user_agent}
maoyan_url = 'https://maoyan.com/films?showType=3'
response = requests.get(maoyan_url, headers = header)
bs_info = bs(response.text, 'html.parser')

data_list = []
for tag in bs_info.find_all('div', attrs={'class': 'movie-hover-info'},limit=10):
    movie_name = tag.find('span', attrs={'class': 'name'}).text
    movie_type = tag.find('span', text='类型:').parent.text.split(":")[1].replace('\n', '').replace('\r', '').strip()
    movie_date = tag.find('span', text='上映时间:').parent.text.split(":")[1].replace('\n', '').replace('\r', '').strip()
    movie_info = [movie_name, movie_type, movie_date]
    data_list.append(movie_info)
maoyao_movie_data = pd.DataFrame(data = data_list)
maoyao_movie_data.to_csv('./maoyan_top_10_movie.csv', encoding='utf8', index=False, header=False)
