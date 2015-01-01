#! /usr/bin/env python
import cgitb
cgitb.enable()
import cgi
import yate
import athletemodel

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
if "which_athlete" not in form_data:
    print "<H1>Error</H1>"
    print "Please choose one athlete."
athlete_name = form_data["which_athlete"].value
the_athlete = athletes[athlete_name]

print yate.start_response()
print yate.include_header("Coach Kelly's Timing Data")
print yate.header("Athlete:" + athlete_name + ", DOB:" + the_athlete.dob + ".")
print yate.para("The top times for " + athlete_name + " are:")
print yate.u_list(the_athlete.top3)
print yate.include_footer({"Home":"index.html", "Select another athlete":"generate_list.py"})
