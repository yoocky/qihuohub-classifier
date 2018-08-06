# coding:utf-8

from bs4 import BeautifulSoup
import requests
import os
from Tools import savefile
# 财经资讯语料库路径
corpus_path = "./train_corpus/C2-Financial/"  
start = 338000
end = 339000
for file_name in range(start, end):
    url = 'https://wallstreetcn.com/articles/' + str(file_name)
    res = requests.get(url)
    html = res.text  # 服务器返回响应
    """
    demo 表示被解析的html格式的内容
    html.parser表示解析用的解析器
    """
    soup = BeautifulSoup(html, "html.parser")
    soup_content = soup.find_all("div", class_="node-article-content")
    if soup_content:
       text = soup_content[0].get_text()
       print(corpus_path + str(file_name) + '.txt')
       savefile(corpus_path + str(file_name) + '.txt', text.encode('utf-8'))