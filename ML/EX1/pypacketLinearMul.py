import numpy as np
import pandas as pd
from sklearn import linear_model

matrixA=pd.read_csv("/Users/yifei.hu/Downloads/machine-learning-ex1 PY/ex1/ex1data2.txt",delimiter=',',names=['size','nameOfb','price'])
#matrixA=(matrixA-matrixA.mean())/matrixA.std()
cols = matrixA.shape[1] #获取列数，shape返回一个元组(行，列)
x = matrixA.iloc[:, 0:cols - 1] #把特征行单独拿出
y = matrixA.iloc[:, cols - 1: cols]#把结果行单独拿出
x=np.matrix(x.values)
y=np.matrix(y.values)

model=linear_model.LinearRegression()
model.fit(x,y)

k=model.coef_
b=model.intercept_
print(k,b)