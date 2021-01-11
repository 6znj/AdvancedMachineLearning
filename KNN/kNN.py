# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    KNN algorithm

    author:Yang Liu

    use KNN algorithm to achieve digital recognition
"""

import numpy as np
from os import listdir


# 读取32*32图像文本,转为向量返回
def img2vector(filename):
    retVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            retVect[0, 32 * i + j] = int(lineStr[j])
    return retVect


# 预处理训练集和数据集，将图片文本向量化
def preprocessing():
    # 训练集
    trainFileList = listdir("trainingData/")
    m_train = len(trainFileList)
    trainData = np.zeros((m_train, 1024))
    trainLabel = []
    for i in range(m_train):
        trainData[i, :] = img2vector("trainingData/" + trainFileList[i])
        trainLabel.append(int(trainFileList[i].split('_')[0]))
    trainLabel = np.array(trainLabel)

    # 测试集
    testFileList = listdir("testData/")
    m_test = len(test