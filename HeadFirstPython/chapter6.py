# sanitize
def sanitize(time_string):
    if "-" in time_string:
        (m, s) = time_string.split("-", 1)
    elif ":" in time_string:
        (m, s) = time_string.split(":", 1)
    else:
        return time_string
    return (m + "." + s)

# define a class to store data of athlete
class Athlete:
    def __init__(self, name, dob=None, times=[]):
        self.name = name
        self.dob = dob
        self.times = times
    def top3(self):
        return sorted(set([float(sanitize(s)) for s in self.times]))[0:3]
    def add_time(self, a_time):
        self.times.append(a_time)
    def add_times(self, times):
        self.times.extend(times)


# read file and return an Athlete object
def get_coach_data(filename):
    try:
        with open(filename) as data:
            data_list = data.readline().strip().split(",")
            return Athlete(data_list.pop(0), data_list.pop(0), data_list)
    except IOError as error:
        print("File error: " + str(error))
        return None

# print result
def show_result(athlete):
    print(athlete.name + "'s times are: " + str(athlete.times) + ",\nand the fastest times are: " + str(athlete.top3()))

# define a class inherit list
class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)
    def top3(self):
        return sorted(set([sanitize(s) for s in self]))[0:3]

show_result(get_coach_data("julie2.txt"))
show_result(get_coach_data("james2.txt"))
show_result(get_coach_data("sarah2.txt"))
show_result(get_coach_data("mikey2.txt"))

vera = AthleteList('Vera Y')
vera.append('1.31')
vera.extend(['2.22', '1-21', '2:22'])
print vera
print vera.top3()
"""
# read file and return a dictionary
def get_coach_data(filename):
    dic = dict()
    try:
        with open(filename) as data:
            data_list = data.readline().strip().split(",")
            (dic['name'], dic['dob'], dic['times']) = (data_list.pop(0), data_list.pop(0), sorted(set([float(sanitize(s)) for s in data_list]))[0:3])
            return dic
    except IOError as error:
        print("File Error: " + str(error))
        return None

# print the result
def show_fatest_times(dic):
    print (dic['name'] + "'s fastest times are: " + str(dic['times']))


sarah = get_coach_data("sarah2.txt")
julie = get_coach_data("julie2.txt")
mikey = get_coach_data("mikey2.txt")
james = get_coach_data("james2.txt")

show_fatest_times(sarah)
show_fatest_times(julie)
show_fatest_times(mikey)
show_fatest_times(james)

"""
