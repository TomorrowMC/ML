import glob
import math
import shutil
import sys
import zlib
from timeit import Timer


class abc:
    def g(self):
        global num
        num=5
bbb = abc()
bbb.g()  #需要先调用该方法，否则num不会被创建
print(num)



if True:
    msg="good"

print(msg)

# glob的测试
print(glob.glob("/Users/yifei.hu/Downloads/*.md"))

print(sys.argv)

# 压缩测试
s=b'good sdafasdf dasfasfas'
print(len(s))
t=zlib.compress(s)
print(len(t))
print(t)

#性能测试
print(Timer('a=1; b=2;t=a; a=b; b=t').timeit())

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> average([20, 30, 70])
     40.0
    """
    return sum(values) / len(values)

import doctest

doctest.testmod()

print(math.sqrt(8))