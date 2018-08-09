#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@version: python3.6
@file: NBayes_Predict.py
@software: PyCharm
"""

import jieba
import pickle
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB  # 导入多项式贝叶斯算法
from sklearn.datasets.base import Bunch
from sklearn.feature_extraction.text import TfidfVectorizer
from Tools import writebunchobj, readbunchobj, savefile, readfile

def corpus_segment(filename):
    # 对上传文件进行分词
    corpus_path = "./upload_corpus/" + filename + ".txt" # 未分词分类语料库路径
    seg_path = "./upload_corpus_seg/" + filename + ".txt" # 分词后分类语料库路径
    '''
    corpus_path是未分词语料库路径
    seg_path是分词后语料库存储路径
    '''
    content = readfile(corpus_path)  # 读取文件内容
    '''此时，content里面存贮的是原文本的所有字符，例如多余的空格、空行、回车等等，
    接下来，我们需要把这些无关痛痒的字符统统去掉，变成只有标点符号做间隔的紧凑的文本内容
    '''
    content = content.replace('\r\n'.encode('utf-8'), ''.encode('utf-8')).strip()  # 删除换行
    content = content.replace(' '.encode('utf-8'), ''.encode('utf-8')).strip()  # 删除空行、多余的空格
    content_seg = jieba.cut(content)  # 为文件内容分词
    savefile(seg_path, ' '.join(content_seg).encode('utf-8'))  # 将处理后的文件保存到分词后语料目录

def corpus2Bunch(filename):
    wordbag_path = "upload_word_bag/" + filename + "_set.dat"  # Bunch存储路径
    seg_path = "upload_corpus_seg/" + filename + ".txt" # 分词后分类语料库路径
    # 创建一个Bunch实例
    bunch = Bunch(filenames=[seg_path], contents=[readfile(seg_path)])
    '''
    extend(addlist)是python list中的函数，意思是用新的list（addlist）去扩充
    原来的list
    '''

    # 将bunch存储到wordbag_path路径中
    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print("构建文本对象结束！！！")

def vector_space(filename):
    stopword_path = "upload_word_bag/hlt_stop_words.txt"
    bunch_path = "upload_word_bag/" + filename + "_set.dat"
    space_path = "upload_word_bag/"+ filename +"space.dat"
    train_tfidf_path = "train_word_bag/tfdifspace.dat"
    stpwrdlst = readfile(stopword_path).splitlines()
    bunch = readbunchobj(bunch_path)
    tfidfspace = Bunch(filenames=bunch.filenames, tdm=[], vocabulary={})
    trainbunch = readbunchobj(train_tfidf_path)
    tfidfspace.vocabulary = trainbunch.vocabulary
    vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True, max_df=0.5, vocabulary=trainbunch.vocabulary)
    tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)

    writebunchobj(space_path, tfidfspace)
    print("if-idf词向量空间实例创建成功！！！")

def predicted(filename):
    corpus_segment(filename)
    corpus2Bunch(filename)
    vector_space(filename)

    # 导入训练集
    trainpath = "train_word_bag/tfdifspace.dat"
    train_set = readbunchobj(trainpath)

    # 导入测试集
    testpath = "upload_word_bag/" + filename + "space.dat"
    test_set = readbunchobj(testpath)

    # 训练分类器：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
    clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)

    # 预测分类结果
    predicted = clf.predict(test_set.tdm)
    return predicted
if __name__ == '__main__':
    print(predicted("test"))
