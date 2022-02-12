str = '123456789'
i=1111
print(isinstance(type(i),type(str)))#False
print(type(str)) #<class 'str'>
print(type(i)=="str")  # False

print(3.14j)
print(str[0:-2])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('---------------------       ---------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


dict1=dict(rod11=1,good=2)
print(dict1)
if (i:= (10+1))<10:
    print(' 111')

i =(1,2,3,40000)
j=(1,2,3,40000)
k={5,6,7,8}
s=[1,2,3,40000]
print(i is j)#对的
print('****************')
print(id(i) == id(j))#对的
print('****************')
print(i is s)#错的
print(' ]]]]]]]]]]]')
print(i is k)#错的
print('****************')
x=1
y=1
print(id(x) is id(y))#对的


