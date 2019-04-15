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
        self.OpenFile()

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
        self.CharDeal()


    def CharDeal(self):
        '''
        去除空格和换行符
        :return:
        '''
        chars = self.reader.strip()
        chars = chars.replace(" ","")
        self.chars = chars.replace("\n","")
        #print(self.chars)
        self.CharsCount()


    def CharsCount(self):
        '''
        匹配字符，存在的则存入字典
        :return:
        '''
        self.result={}
        for i in range(33,126):
            x=chr(i)
            x = self.chars.count(chr(i))    #字符计数
            if x != 0:
                self.result[chr(i)]=x  #添加进字典
        #print(self.result)
        self.CharsSort()


    def CharsSort(self):
        '''
        根据字典values进行排序
        :return:
        '''
        sort = sorted(self.result.items(), key=lambda s:s[1])  #按照values排序
        print("--------- sort by number: ----------")
        for x,y in sort:
            print("char: "+x+"  "+"number:"+str(y))

        sort = sorted(self.result.items(), key=lambda s: s[0])  # 按照key排序
        print("--------- sort by chars: ----------")
        for x, y in sort:
            print("char: " + x + "  " + "number:" + str(y))






def main():
    filename = sys.argv            #获取控制台文件名
    #print(filename[1])
    statistics(filename[1])        #启动




if __name__ == '__main__':
    main()