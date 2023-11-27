
listValues = ['Apple',"Banana", 'cherry', 'Apple','Cherry'];
print(listValues)

# Show len of list
print (len(listValues))

# list contain different type of data type
mixValues = [45, 8.5 , 'a' ,'Apple'];
print (mixValues);

#list constructor
listValues = list(('Apple','Banna','Cherry'))
print (listValues)

def accessItems():
    listValues = ['Pen', 'Pencil','Eraser','Sharpener', 'Note','Book'];
    print ('1st value :', listValues[0])
    print ('2nd value :', listValues[1])
    print ('Reversing ')
    print (listValues[-1]);
    print ('Range of index')
    print (listValues[2:5])
    print (listValues[2:])
    print (listValues[:4])
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)

    thislist = ["apple", "banana", "cherry"]
    for i in [0,1,2]:
        print(thislist[i])
    
accessItems();

def addItems():
    listValues = [78 , 59,56]
    listValues.insert(1,79);
    print (listValues)
    listValues2 =[89,56,74];
    listValues.extend(listValues2);
    print (listValues);
    
addItems()

def removeItems():
    listValues = [78,96,63,32,21,14,47,85]
    listValues.remove(96)
    print (listValues)
    listValues.pop()
    print (listValues)
    del listValues[1];
    print (listValues);
    # del listValues; 
    listValues.clear();
    print (listValues) 

removeItems();

def listsBulitIn(): 
    # list comprehension
    fruits = ["apple", "banana", "cherry", "Kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print(newlist);
    fruits.sort()
    print (fruits)
    fruits.sort(reverse = True)
    print (fruits)
    fruits.sort(key = str.lower)
    print (fruits)
    fruits.reverse();
    print (fruits);
    

listsBulitIn();

def cloneList():
    fruits = ["apple", "banana", "cherry", "Kiwi", "mango", 'clone']
    cloneList = fruits.copy();
    copyList = list(fruits)
    print (cloneList)
    print (copyList)

cloneList();

def joinTwoLists():
    numbers = [1,2,3,4,5,6]
    alphabets = ['a','b','c','d']
    joinLits = numbers +alphabets
    print (joinLits)
    
joinTwoLists();
