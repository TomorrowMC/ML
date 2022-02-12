# 测试一下print表格
import pickle

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3),repr(x*x*x).rjust(4))
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))
# 测试一下print文件内容
f1=open('/Users/yifei.hu/Library/Mobile Documents/iCloud~QReader~MarginStudy/Documents/大二/CPT111/AS/未命名文件夹/Person.txt','r')

while (str1:=f1.readline())!='':
    print(str1)
    print(f1.tell())
pickle.dumps(f1)

class abc:
    y=0
    x:int
    y:int
    def g(self):
        print(self.y)

bbb=abc(1,2)
bbb.g()
