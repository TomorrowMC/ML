import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def cost_function(x,y,thera):
    sum_vector=np.power(x*thera.T-y,2)
    sum=np.sum(sum_vector)
    cost=sum/(2*len(x))
    return cost
def decent(x,y,thera,iters,alpha):
    cost=np.zeros(iters)
    temp = np.matrix(np.zeros(thera.shape))
    for i in range(iters):
        cost[i]=cost_function(x,y,thera)
        for j in range(thera.shape[1]):
            sum=(x[:,j:j+1].T)*(x*(thera.T)-y)
            partial=(alpha/x.shape[0])*sum
            temp[0,j]=thera[0,j]-partial
        thera=temp
    return thera,cost


matrixA=pd.read_csv("/Users/yifei.hu/Downloads/machine-learning-ex1 PY/ex1/ex1data2.txt",delimiter=',',names=['size','nameOfb','price'])
matrixA=(matrixA-matrixA.mean())/matrixA.std()
matrixA.insert(0,'ones',1)
x=matrixA.iloc[:,0:3]
y=matrixA.iloc[:,3:4]
x=np.matrix(x.values)
y=np.matrix(y.values)
thera=np.matrix([[0,0,0]])
iters=1000
alpha=0.1
thera,cost=decent(x,y,thera,iters,alpha)
print(thera)

fig,ax=plt.subplots(figsize=(12,8))
ax.plot(range(iters),cost,'r')
ax.set_xlabel(' times')
ax.set_ylabel(' cost')
ax.set_title('err')
plt.show()

