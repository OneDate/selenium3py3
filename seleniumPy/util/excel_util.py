#!/user/bin/env python    
#-*- coding:utf-8 -*-

import xlrd
import  xlutils
from  xlutils.copy import  copy
'''
操作excel表的类。增加了容错的处理，


'''

class ExcelUtil():
    def __init__(self,filePath= None,sheetIndex=None):

        if filePath == None:
            self.filePath = 'D:/untitled/seleniumPy/config/caseDdt.xls'
        else:
            self.filePath=filePath

        if sheetIndex == None:
            self.sheetIndex = 0
        else:
            self.sheetIndex = sheetIndex

        self.data = self.getData()

    #获取 excel表数据
    def getData(self):
        data = xlrd.open_workbook(self.filePath)
        table = data.sheets()[self.sheetIndex]
        return table

    #获取 行数
    def getRows(self):
        rows =self.data.nrows
        if rows >=1:
            return rows
        return None
    #获取excel表数据，按照每行格式，添加到[]中
    def getValues(self):
        result = []
        rows =  self.getRows ()
        if rows!= None:
            for i in range(rows):
                #获取 一行的数据
                col = self.data.row_values(i)
                result.append(col)
                print(result)
            return result
        return  None

    #获取单元格的数据
    def getDataValue(self,row,coll):
        if self.getRows() >row:
            data = self.data.cell_value(row,coll)
            # print(data)
            return  data
        return None


    #写入数据
    def writeData(self,row,cell,value):
        readData=xlrd.open_workbook ( self.filePath )
        writeData = copy(readData)
        writeData.get_sheet(0).write(row,cell,value)
        writeData.save(self.filePath)

if __name__ == '__main__':
    e = ExcelUtil('D:/untitled/seleniumPy/config/keyWord.xls',0)
    # e.getValues()
    e.getDataValue(1,4)
