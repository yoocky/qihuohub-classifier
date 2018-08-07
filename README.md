# qihuohub-classification
这份工程代码是参照CSDN博客：《[Python中文文本分类](http://blog.csdn.net/github_36326955/article/details/54891204)》的源代码.

运行环境 python3.6

训练集
fetch.py 获取华人街见闻财经资讯，列为C2-Financial分类的语料库


如果你有任何的问题，请在本项目github主页中的issues栏中提出，或者方位上面的博客地址，在下方评论处发布问题。

step1: corpus_segment.py

step2: corpus2Bunch.py
请自觉创建目录train_word_bag和test_word_bag

step3: TFIDF_space.py

step4:NBayes_Predict.py

或直接运行app.py
默认注销掉了训练集的切词，当训练集语料库又增加时，请去掉注释对语料库进行重新切洗词
