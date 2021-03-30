import codecs

string = ""
fileloaded = False

def read(path):
    global string
    global file
    file = codecs.open(path, "r", "utf-8").read()
    global sectionlist
    global sectiondict
    global sectionnames
    global fileloaded
    sectionlist = []
    sectionnames = []
    linelist = file.split("\n")
    while '' in linelist:
        linelist.remove('')

    while ' ' in linelist:
        linelist.remove(' ')
    for line in linelist:
        if "[" in line and "]" in line and not "=" in line:
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


    try:
        if not fileloaded:
            sectionlist.append(sectiondict)
    except:
        pass

    if fileloaded:
        sectionlist.insert(len(sectionlist),sectionlist.pop(0))
    fileloaded = True



def items(section):
    return sectionlist[sectionnames.index(section)]


def sections():
    return sectionnames


def has_section(section):
    if section in sectionnames:
        return True
    else:
        return False


def get(section, variable=0):
    try:
        return sectionlist[sectionnames.index(section)][variable]

    except NameError:
        raise (Exception("No file loaded in memory. Use read() to read file"))

    except KeyError:
        print("Variable " +  str(variable) + " in section " + section + " does not exist")


def clear():
    global string
    string = ""


def write(target, name, file):
    global string
    string += "[" + name + "]" + "\n"

    for item in target:
        string += str(item) + " = " + str(target.get(item)) + "\n"

    file = codecs.open(file, "w", "utf-8")
    file.write(string)
    file.close()
