import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.optimize as opt

def sigmoid(z):
    return (1/(1+np.exp(-z)))#exp代表python中的指数

def cost(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first - second) / (len(X))

def costFunction(theta, x, y):
    theta = np.matrix(theta)
    x = np.matrix(x)
    y = np.matrix(y)
    sum1=((np.log(sigmoid(x*(theta.T)))).T)*y#和中的前一项
    sum2=((np.log(sigmoid(x*(theta.T)))).T)*(1-y)#和中的后一项
    totalSum=-(1/x.shape[0])*(sum1+sum2)
    totalSum=np.sum(totalSum)
    return totalSum

def giantDecent(theta,x,y):
    cost = np.zeros(1001)  # 新建一个全为零的数组，大小为迭代次数
    for i in range(1001):  #循环迭代的次数
        cost[i]=costFunction(theta,x,y)
        print(i,cost[i])#输出一下cost
        temp=theta# 新建一个临时矩阵用于储存theta
        for j in range(theta.shape[1]):# 每个参数循环一次
            xlocs=x[:,j:j+1].T  #第x个参数对应的第x列所有x值。这个需要放到偏导数里面去，所以提前取了T。1x100
            parcialSum=xlocs*((sigmoid(x*(theta.T)))-y)# 偏导数项算出来
            totalParcial=(0.001/x.shape[0])*parcialSum# 每一项的总偏导数
            temp[0,j]=temp[0,j]-totalParcial# 使用临时变量兜着一下更新出来的值
        theta=temp# 统一更新值

    return cost[1000]



def gradient(theta, X, y):
    # 一定要先把它们重新变成一次矩阵
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    parameters = theta.shape[1]#循环的次数，每一个参数都要有步长
    grad = np.zeros(parameters)# 创建一个步长的向量，必须是空值
    for i in range(parameters):#对每一个参数都需要求初始步长
        term = (x[:,i:i+1].T)*(sigmoid(X * (theta.T)) - y)#第i个参数的总误差，算出来的是一个矩阵
        grad[i] = np.sum(term) / len(X)#使用sum把矩阵转化成数字，并求得最终步长，循环所有的参数
    return grad# 返回所有参数的初始步长

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




matrixA=pd.read_csv("/Users/yifei.hu/NoUpdate/ML/EX2/ex2data1.txt",delimiter=',',names=['Exam1','Exam2','Admitted'])

posivite=matrixA[matrixA['Admitted'].isin([1])]#筛选该列中值为1的所有数据
nagetive=matrixA[matrixA['Admitted'].isin([0])]#筛选该列中值为0的所有数据


fig,ax = plt.subplots(figsize=(12,8))# 新建画布
# scatter散点图的内容：x,y,其他（c表示颜色，s表示size,marker表示散点类型，label表示标签）
ax.scatter(posivite['Exam1'],posivite['Exam2'],c='r',s=50,marker='x',label='Admitted')
ax.scatter(nagetive['Exam1'],nagetive['Exam2'],c='k',s=50,marker='o',label='Admitted')

#legend表示图例
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')
plt.show()

theta = np.matrix([[0.00,0.00,0.00]]) #新建一个参数,注意一下一定要使用浮点数
matrixA.insert(0,'Ones',1)# 插入一个一行
print(matrixA.head())#看一下数据
x=matrixA.iloc[:,0:3]  #把matrix拆一下，这个是输入项们
y=matrixA.iloc[:, 3: 4]#这个是输出项们
x=np.matrix(x.values)# 转换成矩阵
y=np.matrix(y.values)


print(gradient(theta, x, y))
result = opt.fmin_tnc(func=cost, x0=theta, fprime=gradient, args=(x, y))
# 参数的含义：需要优化的函数、初始值、优化函数的梯度函数（维数需要和初始值一致），传递给优化函数的参数们、
print(result)  #result是一个元组，元组的第一项是优化以后x0的最终值
print(costFunction(result[0], x, y))#使用优化以后的参数去拟合

theta=np.matrix([result[0]])
print(rate(x,y,theta))

