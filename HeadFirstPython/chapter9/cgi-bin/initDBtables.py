import sqlite3
import glob
import athletemodel
import athletelist


# Get data from current model
def getAthletesObj(file_list):
    result = []
    for each_file in file_list:
        try:
            with open(each_file) as ath_file:
                data = ath_file.readline().strip().split(",")
                athlete = athletelist.AthleteList(data.pop(0), data.pop(0), data)
                result.append(athlete)
        except IOError as err:
            print "File error: ", str(err)
            return None
    return result
data_files = glob.glob("../data/*.txt")
athletes = getAthletesObj(data_files)

# Connection to database
connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

# Insert data
for each_ath in athletes:
    name = each_ath.name
    dob = each_ath.dob

    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
    connection.commit()

# Get id
    cursor.execute("SELECT id FROM athletes WHERE name=? AND DOB=?", (name, dob))
    the_current_id = cursor.fetchone()[0]
    for each_time in each_ath.clean_data:
        cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)", (the_current_id, each_time))
    connection.commit()

print "Database successfully initialized"
connection.close()
