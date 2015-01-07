#! /usr/bin/env python

import cgi
"""
import os
import time
import sys
"""
import cgi
import sqlite3
import yate

print yate.start_response()
"""
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cur_time = time.asctime(time.localtime())

print host, addr, cur_time + ":", method + ":",

"""
form = cgi.FieldStorage()
for each_form_item in form:
    ath_id = each_form_item
    ath_time = form[each_form_item].value

con = sqlite3.connect("coachdata.sqlite")
cursor = con.cursor()
cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)", (ath_id, ath_time))
con.commit()
con.close()

print "Add time successfully"
