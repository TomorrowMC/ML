'''
- [ ] 使用yield写一个斐波纳吉
- [ ] 创建一个列表，并且把他的元素扩大10十倍
- [ ] 创建一个矩阵，行列取反
- [ ] 对列表排序输出
'''
import sys

'''
def fbnj(num):
    times = 0
    a = 0
    b = 1
    while True:
        if times>num:
            return
        yield a
        a,b=b,a+b
        times+=1

f=fbnj(10)
while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
'''

a=[1,2,3,4,5,6,7]
a= [i*10 for i in a]
print(a)

b=[
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

b=[{row[i] for row in b} for i in range(4)]
print(b)

for numbers in reversed(sorted(a)):
    print(numbers)


