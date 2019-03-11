#Takes line from text file as input. Splits the line into two lists.
#Calls buildTruthList function to cnstruct truth table, and uses this table
#as argument to computeTruth function, which returns a list of Boolean values
#after computing each possible combination of Boolean variables from the truth
#table.
def classifier(line):

    #print(line)
    listSplit = line.split("\t", 2)
    #print(listSplit)
    #print(len(listSplit))
    splitP = listSplit[0].split(",")
    numberOfP = len(splitP)
    #print(numberOfP)
    expression = listSplit[1]
    #print(expression)
    #print("-----------------------------------------------------------")

    #Declares and instantiates list to store a 'truth table' of Boolean values
    #based on the number of variabless (Px) for the expression the line has.
    truthList = list()
    buildTruthList(0, numberOfP, truthList)

    #The computeTruth function is called to build the list of truth values
    #that results from each expression calculated.
    boolList = computeTruth(expression, truthList)

    #Control statements will return the appropriate classifier string depending
    #on the content of the list of Booleans.
    if True in boolList and False in boolList:
        truthClass = "Contingency"
    elif True in boolList and not False in boolList:
        truthClass = "Tautology"
    else:
        truthClass = "Contradiction"

    return truthClass

#This function will build a list of lists, the list elements consist of Boolean
#values for every combination based on size. Essentially contructs a truth
#table. Uses recursion, halting when index reaches 2^(size). The for loop
#determines 1 or 0 with floor division and modulos operator to run through
#combinations, loop begins on size integer reached for each recursive call.
def buildTruthList(index, size, table):
    if index == pow(2, size):
        return

    truthValues = list()

    for x in range(size - 1, -1, -1):
        b = bool((index//pow(2, x)) % 2)
        truthValues.append(b)

    table.append(truthValues)
    buildTruthList(index + 1, size, table)

#This function calculates the truth values of propositional statements.
#It takes the expression part of the line from the "q2_in.txt" file as an
#argument as well as a list of lists consisting of truth value combinations.
#Certain substrings of the expression string are replaced to allow the eval()
#function to compute truth values. A list is created to add these values,
#and this list of truth values is returned.
def computeTruth(prop, bValues):

    #print(prop)
    #print(bValues)

#The logical expression is converted to lower case.
    prop = prop.lower()

    #This series of if statements replace certain substrings with the desired
    #values so that a logical expression of type string can be evaluted with
    #eval(). In Python, Boolean "is a substype of the integer type..." they
    #"... behave like the values 0 and 1..." (from Python 3 doc).
    #Therefore, '<=' will yield the same results as logical implication, and
    #'==' for biconditional. Boolean operator 'not' has lower precedence than
    # '<=' and '==', therefore parantheses () are needed to avoid syntax error.
    if 'then' in prop:
        prop = prop.replace('then', "<=")

    if '-' in prop:
        prop = prop.replace('-', 'not')
        numberOfB = len(bValues[0])
        for h in range(0, numberOfB):
            prop = prop.replace('not p'+str(h+1), '(not p'+str(h+1)+')')

    if 'eq' in prop:
        prop = prop.replace('eq', '==')

    if 'false' in prop:
        prop = prop.replace('false', 'False')

    if 'true' in prop:
        prop = prop.replace('true', 'True')

    boolList = list()
    variableProp = prop
    print(variableProp)
    #The now lower case variable names 'px' are replaced with Boolean values.
    #Shit, the variables need to be put back the way the were in outer loop.
    for k in range (0, len(bValues)):
        booleanKey = bValues[k]
        for g in range(0, len(booleanKey)):
            prop = prop.replace('p'+str((g+1)), str(booleanKey[g]))
        #print(prop)
        #print(eval(prop))
        boolList.append(eval(prop))
        prop = variableProp

    print(boolList)
    return boolList

outFile = open("q2_out.txt","w+")

#Reads the lines from the open file. The for loop calls the function to
#classifier function to classify them. Prints the result and writes it to
#an output text file.
with open('q2_in.txt','r') as logic:
    lines = logic.readlines()
    for x in range(0, len(lines)):
        stringC = classifier(lines[x])
        print(stringC)
        outFile.write(stringC+"\n")
