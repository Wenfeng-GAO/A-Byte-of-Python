james = []
julie = []
mikey = []
sarah = []
# sanitize
def sanitize(time_string):
    if "-" in time_string:
        (m, s) = time_string.split("-", 1)
    elif ":" in time_string:
        (m, s) = time_string.split(":", 1)
    else:
        return time_string
    return (m + "." + s)
# read file
def get_coach_data(filename):
    try:
        with open(filename) as data:
            return data.readline().strip().split(",")
    except IOError as error:
        print("File Error: " + str(error))
        return None

james = get_coach_data("coachkellysdata/james.txt")
julie = get_coach_data("coachkellysdata/julie.txt")
mikey = get_coach_data("coachkellysdata/mikey.txt")
sarah = get_coach_data("coachkellysdata/sarah.txt")

print(sorted(set([float(sanitize(t)) for t in james]), reverse=True)[0:3])
print(sorted(set([float(sanitize(t)) for t in julie]))[0:3])
print(sorted(set([float(sanitize(t)) for t in mikey]))[0:3])
print(sorted(set([float(sanitize(t)) for t in sarah]))[0:3])
"""
try:
    with open("coachkellysdata/james.txt", "r+") as data_james, open("coachkellysdata/julie.txt", "r+") as data_julie, open("coachkellysdata/mikey.txt", "r+") as data_mikey, open("coachkellysdata/sarah.txt", "r+") as data_sarah:
          james = data_james.readline().strip().split(",")
          julie = data_julie.readline().strip().split(",")
          mikey = data_mikey.readline().strip().split(",")
          sarah = data_sarah.readline().strip().split(",")
except IOError:
    print "Cannot open or write file"
#sorted_james = sorted(james)
#sorted_julie = sorted(julie)
#sorted_mikey = sorted(mikey)
#sorted_sarah = sorted(sarah)
#print sorted_james

# sort

data = [6, 3, 1, 2, 4, 5]
data2 = sorted(data)
print data2
print data
data.sort()
print data



sanitize_james = []
for time in james:
    sanitize_james.append(sanitize(time))


clean_julie = [float(sanitize(time)) for time in julie]
clean_james = [float(sanitize(time)) for time in james]
clean_mikey = [float(sanitize(time)) for time in mikey]
clean_sarah = [float(sanitize(time)) for time in sarah]

unique_julie = []
#unique_james = []
unique_mikey = []
unique_sarah = []
for t in clean_julie:
    if t not in unique_julie:
        unique_julie.append(t)

unique_james = set(clean_james)
print "Unique James: ", unique_james
print "Unique Julie: ", sorted(unique_julie)[0:3]
"""
