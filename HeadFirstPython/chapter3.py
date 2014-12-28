import os
"""
print os.getcwd()
os.chdir('../')
print os.getcwd()
os.chdir('HeadFirstPython')
print os.getcwd()
"""
try:
    data = open("testForChp3.txt")
    print(data.readline())
    print data.tell()
    data.seek(0)
    print data.tell()
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            print "%s said: %s" % (role, line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
