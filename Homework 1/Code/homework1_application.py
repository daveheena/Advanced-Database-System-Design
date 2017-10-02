# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:55:35 2017

@author: Heena
"""

import sqlite3 
from bottle import route, run, template, request

@route("/")
@route("/index.html")
@route("/tasks")
def tasks():
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks')
    result = cursor.fetchall()
    cursor.close()
    output = template('display_tasks', rows=result)
    return output

@route("/addtask",method="GET")
def addtask():
    return template('add_task')

@route("/addtask",method="POST")
def addnewtask():
    newtask = request.POST.get('task_name','').strip()
    
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks(task_name,task_status,task_priority) VALUES(?,?,?)",(newtask,"New",1))
    connection.commit()
    cid = cursor.lastrowid
    cursor.close()
    if cid != 0:
        return "<p>The task is successfully added.</p>"
    else:
        return "<p>The task is not added.</p>"

@route("/edittask",method="GET")
def edittask():
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks where task_status != "Completed"')
    result = cursor.fetchall()
    output = template('edit_task',rows=result)
    cursor.close()
    return output

@route("/edittask",method="POST")
def edittask_post():
    task = "" + request.POST.get('task_name','').strip()
    newtask = "" + request.POST.get('new_task_name','').strip()
    status = request.POST.get('task_status','').strip()
    priority = request.POST.get('task_priority','').strip()
    
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET task_name= ? ,task_status= ? ,task_priority= ? WHERE id LIKE ?",(newtask,status,priority,task))
    connection.commit()
    cid = cursor.lastrowid
    cursor.close()
    if cid != 0:
        return "<p>The task is successfully updated.</p>"
    else:
        return "<p>The task is not updated.</p>"
    
@route("/deletetask",method="GET")
def deletetask():
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks')
    result = cursor.fetchall()
    output = template('delete_task',rows=result)
    cursor.close()
    return output

@route("/deletetask",method="POST")
def deletetask_post():
    task = "" + request.POST.get('task_name','').strip()
    
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tasks WHERE id LIKE ?',task)
    connection.commit()
    cid = cursor.lastrowid
    cursor.close()
    if cid != 0:
        return "<p>The task is successfully deleted.</p>"
    else:
        return "<p>The task is not deleted.</p>"
    
run(host='localhost',port=8080, reloader=True)
    