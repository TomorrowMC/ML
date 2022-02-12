import numpy as np
import pandas as pd

matrixA = pd.read_csv("/Users/yifei.hu/Downloads/machine-learning-ex1 PY/ex1/ex1data1.txt",names=['population', 'profit'], delimiter=',') #使用pandas读取csv
matrixA.insert(0, 'One', 1)
cols = matrixA.shape[1] #获取列数，shape返回一个元组(行，列)
x = matrixA.iloc[:, 0:cols - 1] #把特征行单独拿出
y = matrixA.iloc[:, cols - 1: cols]#把结果行单独拿出
x=np.matrix(x.values)
y=np.matrix(y.values)

thera=np.linalg.inv((x.T)*x)*(x.T)*y
print(thera)