import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.optimize as opt

def sigmoid(z):
    return (1/(1+np.exp(-z)))#exp代表python中的指数
def cost(theta, X, y, learningRate):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    reg = (learningRate / (2 * len(X))) * np.sum(np.power(theta[:,1:theta.shape[1]], 2))
    return np.sum(first - second) / len(X) + reg

# 和上一题一样，计算一下初试梯度
def gradientReg(theta, X, y, learningRate):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)
    error = sigmoid(X * theta.T) - y
    for i in range(parameters):
        term = np.multiply(error, X[:, i])
        if (i == 0):
            grad[i] = np.sum(term) / len(X)
        else:
            grad[i] = (np.sum(term) / len(X)) + ((learningRate / len(X)) * theta[:, i])
    return grad


def predict(thera,x):#预测输入的x最终的结果,thera是参数，x是矩阵
    probability=sigmoid(np.sum(x*(thera.T)))# x是1x3，thera是1x3
    if probability>=0.5:
        return 1
    else:
        return 0

def rate(x,y,thera):#x是插入1列以后的所有输入列nxm，y是所有输出列nx1，thera是参数列1xm
    totalNumber=x.shape[0]
    correct=0
    for i in range(x.shape[0]):
        predictNum=predict(thera,x[i])
        knowNum=np.sum(y[i,0])
        if predictNum==knowNum:
            correct=correct+1
    rate=correct/totalNumber
    result=f'accuracy= {rate}'
    return result
# 读取和显示所有的参数
path =  '/Users/yifei.hu/NoUpdate/ML/EX2/ex2data2.txt'
data2 = pd.read_csv(path, header=None, names=['Test 1', 'Test 2', 'Accepted'])
print(data2.head())

positive = data2[data2['Accepted'].isin([1])]
negative = data2[data2['Accepted'].isin([0])]

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(positive['Test 1'], positive['Test 2'], s=50, c='b', marker='o', label='Accepted')
ax.scatter(negative['Test 1'], negative['Test 2'], s=50, c='r', marker='x', label='Rejected')
ax.legend()
ax.set_xlabel('Test 1 Score')
ax.set_ylabel('Test 2 Score')
plt.show()


degree = 5
x1 = data2['Test 1']  #获取表中单独的一列
x2 = data2['Test 2']

data2.insert(3, 'Ones', 1)  #在表中插入一列，位置在第三个地方

# 特征映射，不会就算了，就当创建了很多新特征
for i in range(1, degree):
    for j in range(0, i):
        data2['F' + str(i) + str(j)] = np.power(x1, i-j) * np.power(x2, j)

data2.drop('Test 1', axis=1, inplace=True)# 移除最初的两列
data2.drop('Test 2', axis=1, inplace=True)

data2.head()
# set X and y (remember from above that we moved the label to column 0)
cols = data2.shape[1]
X2 = data2.iloc[:,1:cols]
y2 = data2.iloc[:,0:1]

# convert to numpy arrays and initalize the parameter array theta
X2 = np.array(X2.values)
y2 = np.array(y2.values)
theta2 = np.zeros(11)
learningRate = 1


#
print(cost(theta2, X2, y2, learningRate))#计算初始cost
print(gradientReg(theta2, X2, y2, learningRate))#计算初始梯度
result2 = opt.fmin_tnc(func=cost, x0=theta2, fprime=gradientReg, args=(X2, y2, learningRate))

theta_min = np.matrix([result2[0]])
predictions = rate( X2,y2,theta_min)
print(predictions)

from sklearn import linear_model#调用sklearn的线性回归包
model = linear_model.LogisticRegression(penalty='l2', C=1.0)
model.fit(X2, y2.ravel())
model.score(X2, y2)# 查看结果
k=model.coef_
b=model.intercept_
print(k,b)#获取参数

