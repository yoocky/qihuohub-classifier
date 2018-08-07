#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@version: python3.6
@author: yoocky
@contact: mengyanzhou@gmail.com
@file: fetch.py
@time: 2018/8/4 16:12
@software: PyCharm
"""
from bs4 import BeautifulSoup
import requests
import os
from Tools import savefile

# 财经资讯语料库抓取
corpus_path = "./train_corpus/C2-Financial/C2-Financial" 
count = 0 
start = 338000
end = 338100
for article_id in range(start, end):
    url = 'https://wallstreetcn.com/articles/' + str(article_id)
    res = requests.get(url)
    html = res.text
    """
    soup 表示被解析的html格式的内容
    html.parser表示解析用的解析器
    """
    soup = BeautifulSoup(html, "html.parser")
    soup_content = soup.find_all("div", class_="node-article-content")
    if soup_content:
       text = soup_content[0].get_text()
       count += 1
       file_path = corpus_path + str(count) + '.txt'
       savefile(file_path, text.encode('utf-8'))
       print(text)
       print(file_path)