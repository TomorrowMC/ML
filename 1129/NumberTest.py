import math
import random




if __name__ == '__main__':
    # 截断测试
    a = math.pi
    b = int(a)
    print(b)
    # 测试math方法
    t1 = math.modf(a)
    print(t1[0])
    print(t1[1])
    g = random.uniform(1, 3)
    random.seed()
    print(g)
    # 测试奇进偶退
    del a, b
    a = 10.5
    b = 11.5
    c = '一'
    print(round(a))  # 10
    print(round(b))  # 12
    # 测试格式化字符
    print('什么%s玩意' % ('寄吧'))
    print(f'{1+1=}')
    print(c.isnumeric())
    del a, b, c
    site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
    pop_obj = site.popitem()
    print(pop_obj)
    print(type(pop_obj))
    print(site)
    print('*********')
    a = [0, 2, 3, 4, 5]
    a.remove(0)
    print(a)
    print(1)
    c = 1
    while c < 6:
        if c == 4:
            print(c)
            break

        else:
            c += 1
            continue
    del a,c
    print(1,2)
