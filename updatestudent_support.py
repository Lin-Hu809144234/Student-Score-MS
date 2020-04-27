#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 02, 2020 11:01:39 PM CST  platform: Windows NT

import sys
import pymysql

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

def comeback():
    destroy_window()
    sys.stdout.flush()

def updatestudent():
    sno = w.Entry1.get()
    sname = w.Entry2.get()
    dept = w.Entry3.get()
    major = w.Entry4.get()
    class1 = w.Entry5.get()
    g1 = w.Entry6.get()
    conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
    cur = conn.cursor()
    values = [sname,dept,major,class1,g1,sno]
    cur.execute('select * from student where sno = %s',sno)
    r = cur.fetchone()
    if r != None:
        cur.execute('update student set sname = %s,sex = %s,sage = %s,dept = %s,class = %s where sno = %s',values)
        v.showinfo('successful',sname+'同学信息更新成功')
        conn.commit()
        cur.close()
        conn.close()
        destroy_window()
    else:
        v.showerror('error',sname+'同学信息不存在，请确认')
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
    import updatestudent
    updatestudent.vp_start_gui()




