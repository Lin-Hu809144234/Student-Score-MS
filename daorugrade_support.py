#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 03, 2020 12:31:38 AM CST  platform: Windows NT

import sys
import pymysql
import xlrd
from tkinter import filedialog as a

try:
    import Tkinter as tk
    import Tkinter.messagebox as v
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as v

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def daoru():
    f = a.askopenfilename(filetypes = [("XLSX",".xlsx")])
    book = xlrd.open_workbook(f)
    w.Entry_url.insert(0,f)
    sheet = book.sheet_by_name("Sheet1")
    conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
    cur = conn.cursor()
    query2 = 'insert into class(cno,cname,credit) values(%s,%s,%s)'
    query1 = 'insert into student(sno,sname,sex,sage,dept,class) values(%s,%s,%s,%s,%s,%s)'
    query3 = 'insert into grade(sno,cno,grade) values(%s,%s,%s)'
    for r in range(1,sheet.nrows):
        sno = sheet.cell(r,0).value
        sname = sheet.cell(r,1).value
        sex = sheet.cell(r, 2).value
        sage = sheet.cell(r, 3).value
        dept = sheet.cell(r, 4).value
        class1 = sheet.cell(r, 5).value
        cno = sheet.cell(r, 6).value
        cname = sheet.cell(r,7).value
        credit = sheet.cell(r,8).value
        grade = sheet.cell(r,9).value
        cur.execute('select cno from class where cno = %s',cno)
        r2 = cur.fetchone()
        cur.execute('select sno from student where sno = %s', sno)
        r1 = cur.fetchone()
        if r1 == None and r2 == None:
            values2 = (cno,cname,credit)
            cur.execute(query2, values2)
            values1 = (sno,sname,sex,sage,dept,class1)
            cur.execute(query1, values1)
            values3 = (sno,cno,grade)
            cur.execute(query3, values3)
        elif r1 == None and r2 != None:
            values1 = (sno,sname,sex,sage,dept,class1)
            cur.execute(query1, values1)
            values3 = (sno,cno,grade)
            cur.execute(query3, values3)
            v.showerror('提示',cname+'课程已经存在,无需再添加')
        elif r1 != None and r2 == None:
            values2 = (cno,cname,credit)
            cur.execute(query2, values2)
            values3 = (sno,cno,grade)
            cur.execute(query3, values3)
            v.showerror('提示',sno+'学生信息已经存在，无需再添加')
        else:
            values3 = (sno,cno,grade)
            cur.execute(query3, values3)
    conn.commit()
    cur.close()
    conn.close()
    columns = str(sheet.ncols)
    rows = str(sheet.nrows)
    print("导入 " +columns + " 列 " + rows + " 行数据到MySQL数据库!")
    sys.stdout.flush()
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import daorugrade
    daorugrade.vp_start_gui()




