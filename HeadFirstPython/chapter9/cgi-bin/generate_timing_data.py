#! /usr/bin/env python
import cgitb
cgitb.enable()
import cgi
import yate
import athletemodel

form_data = cgi.FieldStorage()
if "which_athlete" not in form_data:
    print "<H1>Error</H1>"
    print "Please choose one athlete."
athlete_id = form_data["which_athlete"].value
athlete = athletemodel.get_athlete_from_id(athlete_id)

print yate.start_response()
print yate.include_header("Coach Kelly's Timing Data")
print yate.header("Athlete:" + athlete['name'] + ", DOB:" + athlete['dob'] + ".")
print yate.para("The top times for " + athlete['name'] + " are:")
print yate.u_list(athlete['top3'])
print yate.para("The entire set of timing data is: " + str([float(item) for item in athlete['data']]) + " (duplicates removed).")
print yate.do_form("add_time.py", ['add_time'], "post", "Add a new time");
print yate.include_footer({"Home":"../index.html", "Select another athlete":"generate_list.py"})
