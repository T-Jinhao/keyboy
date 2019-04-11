#!/usr/bin/python
#encoding=utf8

'''
字符统计并排序
字符统计范围：ASCII码33-126，中文不能匹配
'''


import sys


class statistics():

    def __init__(self,name):  #赋予文件名
        self.name=name

    def OpenFile(self):
        '''
        打开文件
        :return:
        '''
        with open(self.name,'r') as f:
            try:
                self.reader = f.read()

            except:
                print("Can't open "+self.name)
                exit()


    def CharDeal(self):
        '''
        去除空格和换行符
        :return:
        '''
        chars = self.reader.strip()
        chars = chars.replace(" ","")
        self.chars = chars.replace("\n","")
        #print(self.chars)


    def CharsCount(self):
        '''
        匹配字符，存在的则存入字典
        :return:
        '''
        self.result={}
        for i in range(33,126):
            x=chr(i)
            x = self.chars.count(chr(i))
            if x != 0:
                self.result[chr(i)]=str(x)  #添加进字典
        #print(self.result)


    def CharsSort(self):
        '''
        根据字典values进行排序
        :return:
        '''
        sort = sorted(self.result.items(),key=lambda item:item[1])
        str="字符数由小到大"
        str=str.decode("utf-8")
        print(str)
        print(sort)




def main():
    filename = sys.argv            #获取控制台文件名
    #print(filename[1])
    file=statistics(filename[1])   #获取文件名
    file.OpenFile()                #打开文件
    file.CharDeal()                #去掉空格换行符
    file.CharsCount()              #字符计数
    file.CharsSort()               #按照字符数排序



if __name__ == '__main__':
    main()