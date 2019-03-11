#This function replaces the T or F characters with Boolean values.
def replaceValue(x):
    if x == 'T':
        return 'True'
    else:
        return 'False'

#This function calculates the truth value for propositional statements.
#It takes a line from the 'q1_in' file as an argument and splits it into
#a list of three strings. The assigned truth values found in the list are
#split into a list. The list characters of 'T' and 'F' are replaced with
#Boolean values. The eval() function evaluates the expression and returns
#the resulting truth value.
def computeTruth(exp):
    print(exp)
    listSplit = exp.split("\t", 3)
    #print(listSplit)
    valueSplit = listSplit[1].split(",")
    #print(valueSplit)
    L = list()

    #For loop calls the facilitator method to replace characters with Booleans.
    for y in range(len(valueSplit)):
        L.append(replaceValue(valueSplit[y]))
#L is the list of Boolean values.
    #print(L)

#The prop variable is the propositional expression of the line. Converted
#to lowercase to easily replace substrings.
    prop = listSplit[2]
    prop = prop.lower()

    #The series of if statements replace certain substrings with the desired
    #values so that a logical expression of type string can be evaluted with
    #eval(). In Python, Boolean "is a substype of the integer type..." they
    #"... behave like the values 0 and 1...". Therefore, '<=' will yield
    #the same results as logical implication, and '==' for biconditional.
    if 'then' in prop:
        prop = prop.replace('then', "<=")

    if '-' in prop:
        prop = prop.replace('-', 'not')

    if 'eq' in prop:
        prop = prop.replace('eq', '==')

    if 'false' in prop:
        prop = prop.replace('false', 'False')

    if 'true' in prop:
        prop = prop.replace('true', 'True')

    #The now lower case variable names 'px' are replaced with Boolean values.
    for g in range(0, len(L)):
        prop = prop.replace('p'+str((g+1)), L[g])

    print(prop)
    print(eval(prop))
    return eval(prop)

#Creates output file
outFile = open("q1_out.txt","w+")

#Reads the lines from the open file. The for loop calls the function to
#calculate the truth value for each line and writes it to an output file.
with open('q1_in.txt','r') as logic:
    lines = logic.readlines()
    for x in range(0, len(lines)):
        stringB = computeTruth(lines[x])
        outFile.write(str(stringB)+'\n')

