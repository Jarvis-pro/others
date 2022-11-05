import pandas as pd
import os
import numpy as np
from pandas import Series,DataFrame,concat

Folder_Path = r'C:\Users\Jarvis\Desktop\Li\18650\四线法数据\温度阻抗频率\1\15-60'          #要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path =  r'C:\Users\Jarvis\Desktop\Li\18650\四线法数据\温度阻抗频率\1\15-60\deal'       #拼接后要保存的文件路径
SaveFile_Name = r'all.csv'              #合并后要保存的文件名
Last = r'last.csv'

#修改当前工作目录
os.chdir(Folder_Path)
#将该文件夹下的所有文件名存入一个列表

file_list = ['imp1.csv','imp2.csv','imp3.csv','imp4.csv','imp5.csv','imp6.csv','imp7.csv','imp8.csv','imp9.csv','imp10.csv',
'imp11.csv','imp12.csv','imp13.csv','imp14.csv','imp15.csv','imp16.csv','imp17.csv','imp18.csv','imp19.csv','imp20.csv',
'imp21.csv','imp22.csv','imp23.csv','imp24.csv','imp25.csv','imp26.csv','imp27.csv','imp28.csv','imp29.csv','imp30.csv',
'imp31.csv','imp32.csv','imp33.csv','imp34.csv','imp35.csv','imp36.csv','imp37.csv','imp38.csv','imp39.csv','imp40.csv',
'imp41.csv','imp42.csv','imp43.csv','imp44.csv','imp45.csv','imp46.csv','imp47.csv','imp48.csv']

#读取第一个CSV文件并包含表头
df = pd.read_csv(Folder_Path +'\\'+ file_list[0], header=12)   #编码默认UTF-8，若乱码自行更改

#将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False)

#循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1,len(file_list)):
    dfi = pd.read_csv(Folder_Path + '\\'+ file_list[i], header=12)
    df = pd.concat([df,dfi],axis=1)
    df.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig", index=True, header=True, mode='a+')

df = df.tail(39)
df.to_csv(SaveFile_Path+'\\'+ Last,encoding="utf_8_sig", index=True, header=True, mode='a+')

print("Successe!")
