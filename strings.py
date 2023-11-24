def multiLineStrings():
    global multiLine ,multiLine1
    multiLine = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""";
    print(multiLine)
    multiLine1 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
    print(multiLine1)
    
    fruits = 'Apple'
    for fruit in fruits:
        print (fruit)
        
multiLineStrings()

print ("String bulit-in function")

def bulitFunction():
    print ('length of ', len(multiLine))
    
bulitFunction();

def checkString():
    print ('find "tempor" :' ,"tempor" in multiLine)
    print ('find "tempor" :' ,"tempor" not in multiLine)
    
checkString()

# string concatenation and format method
def strConcatFormat():
    str1 ='Hello';
    str2 = 'World';
    print(str1+str2)
    age = 45
    permission = 'vote'
    statement ='my name is python, i am {} . i have permission for {}';
    print(statement.format(age,permission));
    quantity = 5;
    itemNumber = 'INOO12'
    amt = 55.25;
    myOrder = "I want to pay {2} INR for {0} pice for item no : {1}";
    print(myOrder.format(quantity,itemNumber,amt)) 
    # def string
    
strConcatFormat()