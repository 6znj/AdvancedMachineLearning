# -*- coding:utf-8 -*-

import numpy as np


# ID3 Decision Tree

class DecisionTree:
    def __init__(self):
        self._tree = None

    def _calcEntropy(self, y):
        """
        计算香农熵
        :param y: 数据集标签
        :return: 香农熵
        """

        num = y.shape[0]
        # 统计y中不同label值的个数，并用字典labelCounts存储
        labelCounts = {}
        for label in y:
            if label not in labelCounts.keys():
                labelCounts[label] = 0
            labelCounts[label] += 1

        # 计算熵
        entropy = 0.0
        for key in labelCounts:
            prop = float(labelCounts[key]) / num
            entro