import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model

matrixA = pd.read_csv("/Users/yifei.hu/Downloads/machine-learning-ex1 PY/ex1/ex1data1.txt",
                      names=['population', 'profit'], delimiter=',')  # 使用pandas读取csv
# matrixA.insert(0, 'One', 1) #插入新列。不能直接插入新行。此处的参数为：第几列插入，插入的列名，列的数值
cols = matrixA.shape[1]  # 获取列数，shape返回一个元组(行，列)
x = matrixA.iloc[:, 0:cols - 1]  # 把特征行单独拿出
y = matrixA.iloc[:, cols - 1: cols]  # 把结果行单独拿出
X = np.matrix(x.values)
y = np.matrix(y.values)  # 把pandas的excel表转换成矩阵

model = linear_model.LinearRegression()
model.fit(X, y)
k = model.coef_
b = model.intercept_
print(k, b)

x = np.array(X[:, X.shape[1] - 1:X.shape[1]])
f = model.predict(X).flatten()
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(matrixA.population, matrixA.profit, label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()
