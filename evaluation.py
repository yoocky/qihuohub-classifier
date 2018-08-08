#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@version: python3.6
@author: yoocky
@contact: mengyanzhou@gmail.com
@file: app.py
@time: 2018/8/4 16:12
@software: PyCharm
"""
import os
# step1 分词操作
os.system("python3 ./corpus_segment.py")
# step2 结构化表示--构建词向量
os.system("python3 ./corpus2Bunch.py")
# step3 权重策略--TF-IDF
os.system("python3 ./TFIDF_space.py")
# step4 调用贝叶斯分类器对测试集进行预测
os.system("python3 ./NBayes_Predict.py")