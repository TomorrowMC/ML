import zlib
from datetime import datetime
import re
import math

fileSource = open('/Users/yifei.hu/Downloads/tempfile.gpx', 'r')  # 第一个路径是GPX文件的位置
fileDes = open('/Users/yifei.hu/Downloads/zuji.csv', 'a+')  # 第一个路径是输出csv文件的位置
fileDes.write('dataTime,locType,longitude,latitude,heading,accuracy,speed,distance,isBackForeground,stepType,altitude')
fileDes.write('\n')
i = 1
latnum = 0
lonnum = 0
intTimeStamp = 0
while (GPSList := fileSource.readlines(1)) != []:
    if i % 3 == 2:
        print(GPSList)  # 测试用
        dataTimeStr = GPSList[0]
        dataTimeOb = datetime.strptime(dataTimeStr, '\t\t<time>%Y-%m-%dT%H:%M:%SZ</time>\n')
        intTimeStamp = int(dataTimeOb.timestamp())
        print(intTimeStamp)  # 测试用
    if i % 3 == 1:
        print(GPSList)  # 测试用
        latStr = GPSList[0]
        pattern = re.compile(r'\d+.\d+')  # 查找数字
        latLonList = pattern.findall(latStr)
        print(latLonList)
        latnum = float(round(float(latLonList[0]), 6))
        lonnum = float(round(float(latLonList[1]), 6))
        print(latnum, lonnum)
    if i % 3 == 0:
        fileDes.write(f'{intTimeStamp},1,{lonnum},{latnum},81.272308,78,0.82,0.000000,0,0,0.000000\n')

    i += 1
fileDes.close()
fileSource.close()


