#! /usr/bin/env python

import cgi
import os
import time
import sys
import yate

print yate.start_response()
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cur_time = time.asctime(time.localtime())

print host, addr, cur_time + ":", method + ":",

form = cgi.FieldStorage()
for each_form_item in form:
    print each_form_item, "->", form[each_form_item].value,
print "OK"