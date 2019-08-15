#!/user/bin/env python    
#-*- coding:utf-8 -*-
from  util.excel_util import  ExcelUtil
from  actionkeyword.actionMathod import ActionMethod
import sys
sys.path.append('D:/untitled/seleniumPy')
'''
关键字驱动，用例总方法
'''

class KeyWordCase():
    def __init__(self):
        self.headle_excel=ExcelUtil ('D:/untitled/seleniumPy/config/keyWord.xls')
        self.action_method=ActionMethod ()

    def run_main(self):

        # 拿到行数
        case_lines = self.headle_excel.getRows()
        if case_lines:
            # 循环行数，执行case
            for i in range(1,case_lines):
                is_run =  self.headle_excel.getDataValue(i,3)
                # 判断是否执行
                if is_run == "yes":
                    # 拿到执行方法
                    method= self.headle_excel.getDataValue ( i ,4 )
                    # 拿到输入数据
                    send_value = self.headle_excel.getDataValue ( i , 5 )
                    # 拿到定位元素
                    operation_value= self.headle_excel.getDataValue ( i , 6 )
                    #预期结果判断方法
                    except_result_method =self.headle_excel.getDataValue(i,7)
                    #预期结果
                    except_result = self.headle_excel.getDataValue(i,8)
                    # 执行方法（输入数据，操作元素）
                    self.run_method(method,send_value,operation_value)
                    if except_result !="":

                        except_values = self.get_except_result_value(except_result)
                        if except_values[0] == 'text':
                            print ( 'except_result_method:::%s' % except_result_method )
                            result = self.run_method(except_result_method)
                            print('result:::%s'%result)
                            if except_values[1] in result:
                                self.headle_excel.writeData(i,9,'pass')
                            else:
                                self.headle_excel.writeData (i,9, 'fail' )
                        elif except_values[0] == 'element':
                            result = self.run_method(except_result_method,except_values[1])
                            if result:
                                self.headle_excel.writeData ( i,9, 'pass' )
                            else:
                                self.headle_excel.writeData (i,9,'fail' )
                        else:
                            #self.headle_excel.writeData ( i , 9 , '没有预期结果' )
                            print('没有预期结果')
                    else:
                        print('预期结果为空')

    #获取预期结果值 一个list，并拆分
    def get_except_result_value(self,data):
        return data.split('=')



    # 根据执行方法，进行判断 查操作
    def run_method(self,method,send_value='',operation_value=''):
        print('sendValues:%s-----operationValue:%s'%(send_value,operation_value))
        result = None
        #返回对象属性值，判断 method对应的值是否在self.action_method中
        method_value = getattr(self.action_method,method)
        if send_value == '' and operation_value =="":
            result=method_value ()
        elif send_value == '' and operation_value!='':
            result=method_value ( operation_value )
        elif send_value != '' and operation_value=='':
            result =method_value ( send_value )
        else:
            result =method_value(send_value,operation_value)
        return  result


if __name__ == '__main__':
    keyW = KeyWordCase()
    keyW.run_main()