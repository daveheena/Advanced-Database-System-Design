# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:44:57 2017

@author: Heena
"""

import sqlite3

connection = sqlite3.connect('tasks.db')
connection.execute('CREATE TABLE tasks (id INTEGER PRIMARY KEY, task_name char(100) NOT NULL, task_status char(30), task_priority INTEGER)')
connection.execute('INSERT INTO tasks (task_name,task_status,task_priority) VALUES("Advanced Database System Design - Home Work","In Progress", 4)')
connection.execute('INSERT INTO tasks (task_name,task_status,task_priority) VALUES("Software Testing - Home Work","Pending", 4)')
connection.execute('INSERT INTO tasks (task_name,task_status,task_priority) VALUES("Parallel and Distributed Algorithm - Quiz","Completed", 5)')
connection.execute('INSERT INTO tasks (task_name,task_status,task_priority) VALUES("Multicore Computing - Mid Term Preparation","Pending", 3)')
connection.commit()