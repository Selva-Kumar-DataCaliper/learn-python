def assingVarible():
    print("Assing value of varible:")
    # varible and datatype declaration
    valueOfInt = 5
    valueOfSting = "string value"
    print(valueOfInt)
    print(valueOfSting)
    # casting
    convertToInt = int(valueOfInt)
    convertToStrsing = str(valueOfInt)
    convertToFloat = float(valueOfInt)
    # get the type
    print("Show type of ", type(convertToInt), type(convertToFloat))


assingVarible()


def caseSensitive():
    a = "a is lower case"
    A = "A is upper case"
    print(a, A)


caseSensitive()


def variableTech():
    # Camel Case
    myVariableName = "this is a camel case varible "

    # Pascal Case
    MyVariableName = "This is Pasal case varible"

    # Snake Case
    my_variable_name = "This is snake case varible"


def multipleVaribles():
    # many values to multiple variables
    x, y, z = "value of string", 9, 9.9
    print(x)
    print(y)
    print(z)

    # unpack a collection
    groupValues = ["value of string", 9, 9.9]
    x, y, z = groupValues
    print(x)
    print(y)
    print(z)


multipleVaribles()

# global variables
def customFunction():
    global customValue
    customValue = "custom value of string"
    print("Local acess of customValue :", customValue)


customFunction()

print("Global acess of customValue :", customValue)

# datatypes of list


def dataTypesList():
    stringValue = "This is string  value"
    intergerValue = 78
    floatValues = 67.91
    print(stringValue, intergerValue, floatValues)
    complexValues = 5j
    print(complexValues)
    # null or none
    assignNull = None
    print(assignNull)
    # boolean varible
    booleanValuePostive = True
    booleanValueNegative = False
    print(booleanValueNegative, booleanValuePostive)

    # list declartion
    listValues = ["stringValue", 1, 3.78, ["apple", "orange"]]
    print(listValues)

    # tuple declartion
    tupleValues = ("Apple", "Banna", "Cherry")
    print(tupleValues)
    
    # dict declartion like for json
    dictValues = {"name": "Student name", "date_of_brith": "05-01-2000"}
    print(dictValues)
    
    # sets declartion like for json
    setValues = {"apple", "banana", "cherry"}
    print(setValues)
    
    # frozen set values declation
    frozensetValues = frozenset({"apple", "banana", "cherry"})
    print('Fronzen set values'+ frozensetValues)


dataTypesList()


def rangeFunction():
    x = range(5)
    print(x)


rangeFunction()