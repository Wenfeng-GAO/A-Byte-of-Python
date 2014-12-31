import pickle

def sanitize(time_string):
    if "-" in time_string:
        (m, s) = time_string.split("_", 1)
    elif ":" in time_string:
        (m, s) = time_string.split(":", 1)
    else:
        return time_string
    return (m + "." + s)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(",")
            return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return None

class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)
    def top3():
        return sorted(set([sanitize(s) for s in self]))[0:3]

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open("athletes.pickle", "wb") as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print("File error (put_and_store): " + str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open("athletes.pickle", "rb") as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print("File error (get_from_store): " + str(ioerr))
    return all_athletes

the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)
#print data
print
#for each_athlete in data:
#    print(data[each_athlete].name + " " + data[each_athlete].dob)
data_copy = get_from_store()
for each_athlete in data_copy:
    athlete = data_copy[each_athlete]
    print athlete.name + " " + athlete.dob

