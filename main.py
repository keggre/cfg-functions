import random
import math
import config

f = open("output.hpp", "w")
g = open("output.sqf", "w")

faces = open("data/faces.txt", "r").readlines()
firstnames = open("data/firstnames.txt", "r").readlines()
glasseses = open("data/glasses.txt", "r").readlines()
lastnames = open("data/lastnames.txt", "r").readlines()
speakers = open("data/speakers.txt", "r").readlines()

def main():
    
    prewrite()
    
    varbs = createVarbs()

    classnames = createClassnames(config.numberOfIdentities)
    createClassList(classnames)

    for item in classnames:

        startClass(item)

        vals = createVals(varbs)

        classBody(varbs, vals)

        endClass()
    
    postwrite()

    print(str(config.numberOfIdentities) + " classes created.")


def prewrite():
    f.write("class CfgIdentities\n{\n")

def postwrite():
    f.write("};")

def calculatePitch():
    rand = random.uniform(0, 1)
    pitch = ((1 / (math.sqrt(2 * math.pi))) ** ((rand ** 2) / (1/4))) / 2
    if random.choice([0,1]) == 1:
        pitch = pitch * -1
    pitch = 1 + (pitch * config.pitchRange)
    pitch = round(pitch, 1)
    return pitch

def selectGlasses(glasses, chanceOfGlasses):
    try:
        if random.uniform(0, 1) > chanceOfGlasses:
            glasses = random.choice(glasseses)
            return glasses
        else :
            return None
    except:
        return None
    
def createName(firstnames, lastnames):
    firstname = random.choice(firstnames)
    lastname = random.choice(lastnames)
    name = firstname.strip() + " " + lastname.strip()
    return name

def startClass(className):
    f.write("\tclass " + className + "\n\t{\n")

def endClass():
    f.write("\t};\n")

def classBody(varbs, vals):
    for num in range(len(varbs)):
        varb = str(varbs[num])
        val = str(vals[num])
        if varb == "pitch":
            f.write('\t\t'+ varb.strip() + ' = ' + val.strip() + ';\n')
        else:
            f.write('\t\t'+ varb.strip() + ' = "' + val.strip() + '";\n')

def createClassList(classList):
    for item in classList:
        g.write(item + "\n")

def createClassnames(numberOfIdentities):
    classnames = []
    for num in range(numberOfIdentities):
        classnames.append(config.tag + '_' + str(num + 1))
    return classnames

def createVarbs():
    varbs = ["face","glasses","name","pitch","speaker"]
    return varbs

def createVals(varbs):
    vals = []
    vals.append(random.choice(faces))
    glasses = selectGlasses(glasseses, config.chanceOfGlasses)
    if glasses == None:
        vals.append("")
    else:
        vals.append(glasses)
    vals.append(createName(firstnames, lastnames))
    vals.append(calculatePitch())
    vals.append(random.choice(speakers))
    return vals


main()
exit()