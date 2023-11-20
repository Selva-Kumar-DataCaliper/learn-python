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

# def string