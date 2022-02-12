import zipfile, os
from itertools import product

# chars = 'abcdefghijklmnopqrstuvwxyz012345678ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+|~{}<>'
#chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars = '1234567890'


def bruteforce(zfile):
    try:
        myzip = zipfile.ZipFile(zfile)
    except FileNotFoundError:
        print('你传入的zip文件不存在')
        return
    global length
    passwords = product(chars, repeat=length)
    for passwd in passwords:
        passwd = ''.join(passwd)
        print(passwd)
        try:
            myzip.extractall(pwd=passwd.encode())
            print('密码破解：', passwd)
            return 1
        except Exception as e:
            print('尝试密码错误：', passwd)


exampleZip = "1111.zip"
for length in range(1, 9):
    a = bruteforce(exampleZip)
    if a == 1:
        break