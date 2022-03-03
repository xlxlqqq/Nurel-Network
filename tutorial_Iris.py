# programmer：xlxlqqq
# time：2022.3.3
# 读取数据集


'''
1.喂入神经网络的数据集必须是乱序的
2.神经网络的训练集和测试集一半4:1
3.每32个数据喂入神经网络，为一个batch

'''

from sklearn import datasets  #sklearn自带了一些经典的数据集
from pandas import DataFrame
import pandas as pd

x_data = datasets.load_iris().data
y_data = datasets.load_iris().target     #读取数据集的label


print("x_data from datasets: \n", x_data)    
print("y_data from datasets: \n", y_data)


x_data = DataFrame(x_data, columns=["花萼长度","花萼宽度","花瓣长度","花瓣宽度"])  #使用数组创建表格（frame）
pd.set_option('Display.unicode.east_asian_width',True)  #使用pandas使列名对齐
print("x_data add index: \n", x_data)

x_data['类别'] = y_data          #表格中新加一列
print("x_data add a column: \n",x_data)





