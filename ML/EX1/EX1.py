import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 单特征代价函数
def costFunction(x, y, thera):
    inner = np.power(((x * (thera.T)) - y), 2)  # 代价函数里面的式子
    # print(inner)
    sum = np.sum(inner / (2 * len(x)))#代价函数外面的式子
    return sum

# 单特征梯度下降
def gradientDecentic(x, y, alpha, times, thera):
    # 传入输出矩阵，输入矩阵，学习率，迭代次数，初始参数
    cost = np.zeros(times)  # 使用np.zreos获取一个规格和times一样的空列表，用于储存迭代的代价函数
    for n in range(0, times):
        cost[n] = costFunction(x, y, thera)
        print([n, cost[n]],thera)
        temp=thera# 避免新建一个额外的矩阵，直接使用thera赋值个临时矩阵（因为需要同步更新，所以需要一个临时矩阵
        #temp= np.matrix(np.zeros(thera.shape))  也可以创建一个空的矩阵，但是比较麻烦了
        for j in range(thera.shape[1]):  # 对于所有的参数进行循环
            xCols=x[:,j:j+1].T   # 取出对偏导数的最后一项（所有xi构成的矩阵的转置）
            inner = xCols*((x * (thera.T)) - y)
            # 先计算出偏导数中前面的一项，即所有样本的预期值和实际值的差距，是一个维数为m的向量。然后乘以xCols，可以算出每一项偏差x这一项特征  的总和，结果是int
            totalSum = (alpha * inner) / (x.shape[0])#把总和乘以1/m和学习率，算出偏导数项
            temp[0,j]=temp[0,j]-totalSum  # 使用temp暂时保存更新以后的该参数，最后再统一更新thera
        thera= temp #循环完一遍以后统一更新thera
    return thera,cost  # 返回最终的值，和cost列表


matrixA = pd.read_csv("/Users/yifei.hu/Downloads/machine-learning-ex1 PY/ex1/ex1data1.txt",
                      names=['population', 'profit'], delimiter=',') #使用pandas读取csv
print(matrixA.head(10))
print(matrixA.describe())# 看一下csv的内容
matrixA.plot(kind='scatter', x='population', y='profit', figsize=(12, 8))# 画一下图像，使用散点图
plt.show()# 显示图像
matrixA.insert(0, 'One', 1) #插入新列。不能直接插入新行。此处的参数为：第几列插入，插入的列名，列的数值
print(matrixA.head(10))#看一下前十行
cols = matrixA.shape[1] #获取列数，shape返回一个元组(行，列)
x = matrixA.iloc[:, 0:cols - 1] #把特征行单独拿出
y = matrixA.iloc[:, cols - 1: cols]#把结果行单独拿出
print(x.head())
print(y.head())#看一下两个数据
x = np.matrix(x.values)
y = np.matrix(y.values)#把pandas的excel表转换成矩阵
thera = np.matrix([[0.00, 0.00]])# 设置一下初始thera参数
print(thera.shape)
print(x.shape)
print(y.shape) #看一下他们的矩阵行列
print(costFunction(x, y, thera))

alpha=0.01
iters=1000
thera,cost = gradientDecentic(x, y, alpha, iters, thera)# 梯度下降，获得最后的thera和每一次的cost
print(thera)


fig, ax = plt.subplots(figsize=(12,8))# 新建一个子画布，大小最好和原有画布一样,参数其实为空也可以。数字越大点越小
x = np.linspace(matrixA.population.min(), matrixA.population.max())#在指定的间隔内返回均匀间隔的数字,用于给f描点
f = thera[0, 0] + (thera[0, 1] * x) #设置函数
ax.plot(x, f, color='y', label='Prediction') #画布上画出f函数，参数为直线的范围，函数公式，颜色,标签

ax.scatter(matrixA.population, matrixA.profit, label='Traning Data')#画布上画散点，参数为x，y，标签

ax.legend(loc=1)# 设置图例的位置，就是标签的位置
# 设置x轴y轴和总标题
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
#展示函数
plt.show()


fig, ax = plt.subplots(figsize=(12,8))
ax.plot(np.arange(iters), cost, 'r') #画一个cost函数和迭代次数的散点图，使用plot连接起来
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')
plt.show()  #展示函数

# 正规方程
def normalEqn(X, y):
    theta = np.linalg.inv(X.T@X)@X.T@y#X.T@X等价于X.T.dot(X)
    return theta
final_theta2=normalEqn(x, y)#感觉和批量梯度下降的theta的值有点差距
print(final_theta2)

#normalThera=(np.linalg.inv(((x.T)*x)))*x.T*y
#print(normalThera)