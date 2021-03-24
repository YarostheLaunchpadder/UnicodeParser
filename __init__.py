import codecs

def read(path):
    global file
    file = codecs.open(path, "r", "utf-8").read()

    global sectionlist
    global sectiondict
    global sectionnames
    sectionlist = []
    sectionnames = []
    linelist = file.split("\n")
    while '' in linelist:
        linelist.remove('')

    for line in linelist:
        if "[" in line and "]" in line:
            try:
                sectionlist.append(sectiondict)

            except:
                pass
            sectiondict = {}
            sectionnames.append(line[1:-1])

        else:
            line = line.replace(" = ", "=")
            line = line.replace("= ", "=")
            line = line.replace(" =", "=")

            sectiondict[line.split('=')[0]] = line.split('=')[1]

    sectionlist.append(sectiondict)

def sections():
    return sectionnames

def get(section, variable=0):
    try:
        return sectionlist[sectionnames.index(section)][variable]

    except NameError:
        raise (Exception("No file loaded in memory. Use read() to read file"))

    except KeyError:
        raise (Exception("Variable does not exist"))


def clear():
    global string
    string = ""


def write(target, name, file):
    global string
    string += "[" + name + "]" + "\n"

    for item in target:
        string += str(item) + " = " + str(myconfig.get(item)) + "\n"

    file = codecs.open(file, "w", "utf-8")
    file.write(string)
    file.close()
    
read("myfile.txt")
print(sectionlist)
