import codecs

file = ""
sections = []
sectiondict = {}
sectionnames = []


def read(path):
    global file
    file = codecs.open(path, "r", "utf-8").read()

    global sections
    global sectiondict
    global sectionnames
    sections = []
    sectionnames = []
    linelist = file.split("\n")
    while '' in linelist:
        linelist.remove('')

    for line in linelist:
        if "[" in line and "]" in line:
            try:
                sections.append(sectiondict)

            except:
                pass
            sectiondict = {}
            sectionnames.append(line[1:-1])

        else:
            line = line.replace(" = ", "=")
            line = line.replace("= ", "=")
            line = line.replace(" =", "=")

            sectiondict[line.split('=')[0]] = line.split('=')[1]

    sections.append(sectiondict)


def get(section, variable=0):
    try:
        return sections[sectionnames.index(section)][variable]

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
    
