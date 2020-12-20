#author : rebeka zhang
# date: 3 Dec 2020
#-*- coding:utf-8 -*-
from hogwarts.songqin.pytest_demo_1202 import *

print('------------准备环境---------')
"""
xlrd xlwt xlutils
"""
#----------1.环境确认-----------------------------------
#----------2.操作excel---------------------------------
#1.请求参数的读取，
import xlrd

excelDir = "./test_cases_API.xls"
#打开excel 文件， formatting_info=True, 保持原样式
workBook = xlrd.open_workbook(excelDir,formatting_info=True)
sheets = workBook.sheet_names() #获取所有的表名
workSheet = workBook.sheet_by_name('获取用户token_1个') #需要执行的sheet

#取数据 获取1行6列的数据
cellData = workSheet.cell(1,6).value
print(cellData)
token = get_token()
res = new_user(token,cellData)
print(res)

if res['message'] == '成功':
    info ='pass'
else:
    info = 'fail'

#2. 测试结果的写入
#文件不存在 -- 新建excel --写 --xlwt
#文件本身存在 -- 另存写新Excel --> xlutils
from xlutils.copy import copy
#1--拷贝excel对象
newWorkBook = copy(workBook)
#2. 取拷贝的excel 的sheet ===sheet的下标
newSheet = newWorkBook.get_sheet(0)
