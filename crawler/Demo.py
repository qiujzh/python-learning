# -*- coding: utf-8 -*-
import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn = cx_Oracle.connect('orcl/orcl@localhost/orcl')
cursor = conn.cursor()
cursor.execute('select * from QDW_CY_NC')
rows = cursor.fetchall()
for row in rows:
    print row[1]