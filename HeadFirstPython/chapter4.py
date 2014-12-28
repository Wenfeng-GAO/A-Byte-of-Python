man = []
other = []
try:
    data = open("testForChp3.txt")
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print "Cannot find file"
#print(man)
#print(other)
try:
    with open("man_data.txt", "w") as data_man, open("other_data.txt", "w") as data_other:
        for each_line in man:
            data_man.write(each_line)
            data_man.write("\n")
        for each_line in other:
            data_other.write(each_line)
            data_other.write("\n")
except IOError:
    print "Cannot find file"

# with
try:
    with open("its.txt", "w") as data:
        data.write("It's...")
except IOError as err:
    print("File error: " + str(err))

with open("man_data.txt") as test:
    print(test.read())
