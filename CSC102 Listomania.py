##########################################################################################################################################################################
#                                                                                                                                                                        #
# Be sure that you take user input for all of your function arguments!                                                                                                   #
# If you do not, you cannot properly test them and neither can your professor to properly grade your assignment!                                                         #
#                                                                                                                                                                        #
# 1. Write a function that takes a list of any size as an argument, and returns a list where all adjacent, equal elements have been reduced to a single element.         #
#       For example [1, 2, 2, 3] would return as [1, 2, 3].                                                                                                              #
# 2. Write a function that takes a list of numbers of any size as an argument and returns true if the list is sorted, and false otherwise.                               #
#       For example, [1, 2, 3] would return True, and [2,1,3] would return false (Hint! Google the Python sorted() function).                                            #
# 3. Write a function that takes a list of numbers of any size as an argument, and returns the sum of the numbers.                                                       #
#       For example, [1,2,2,3] returns 8.                                                                                                                                #
# 4. Write a function that takes a list of any type and size as an argument, and returns a list where the elements are in reverse list order.                            #
#       For example ['rubber', 'baby', 'bellybutton'] returns ['bellybutton', 'baby', 'rubber']                                                                          #
# 5. Write a function that takes two sorted lists as arguments, and returns a single sorted list.                                                                        #
#       For example, providing lists [1, 5, 7] and [1, 2, 4] results in [1,1,2,4,5,7].                                                                                   #
# 6. Write a function that demonstrates and tests each of the above functions.                                                                                           #
#                                                                                                                                                                        #
# Be sure to use comments for both structure of the program and documentation of the code.                                                                               #
# All code must completely be your own individual work product.                                                                                                          #
# Post your Python code file (*.py format) here.                                                                                                                         #
#                                                                                                                                                                        #
##########################################################################################################################################################################

def validPosInput(x):                                                                                                   # checks for valid input and turns it into an int                                                    
    while True:                                                                                                         # this won't accept negative numbers   
        if (str.isdigit(x)):                                                                                            
            x = int(x)                                                                                                  
            break                                                                                                       
        else:                                                                                                           
            x = input('Please select a valid positive integer\n')                                                                
    return x

def validInput(x):                                                                                                      # checks for valid input and turns it into an int
    while True:                                                                                                         # this will accept any number
        if (x.lstrip('-').isdigit()):                                                                                   
            x = int(x)                                                                                                  
            break                                                                                                       
        else:                                                                                                           
            x = input('Please select a valid integer\n')                                                                
    return x

def makeList():                                                                                                         # Creates a list with the users input
    length = input('How many items would you like in your list? ')                                                      # Length of the list is a user input
    length = validPosInput(length)                                                                                      # User inputs each character of the list
    listElement = ''
    listy = []
    for ch in range(1, length +1, 1):
        listElement = input('What would you like in your list? ')
        listy += [listElement]
    return(listy)

def makeNumList():                                                                                                      # Creates a list that only accepts numbers
    length = input('How many items would you like in your list? ')                                                      # Length of the list is a user input
    length = validPosInput(length)                                                                                      # User inputs each character of the list
    listElement = ''
    listy = []
    for ch in range(1, length +1, 1):
        listElement = input('What would you like in your list? ')
        listElement = (validInput(listElement))
        listy += [listElement]
    return(listy)

def listCombine(list1):                                                                                                 # Function that combines all common elements of a list
    combined = []
    for ch in (list1):
        if ch not in combined:
            combined.append(str(ch))
    return(combined)

def checkSorted(list2):                                                                                                 # Checks to see if the list is sorted or not
    if list2 == sorted(list2):
        return(True)
    else:
        return(False)

def listSum(list3):                                                                                                     # Returns the Sum of every int in the list
    return(sum(list3))
    
def listReverse(list4):                                                                                                 # Reverses the order the list is displayed in
    list4.reverse()
    return(list4)
    
def listSingleSorted(list5, list6):                                                                                     # Takes two lists and combines them into a new list
    print('First List: ', list5)                                                                                        # Then sorts the newly formed list and returns it
    print('Second List: ', list6)
    sortedCombinedList = list5 + list6
    sortedCombinedList.sort()
    return(sortedCombinedList)
    
def main():                                                                                                                                     # Defines the main function, this launches all functions
    
    print('Lets make our first list.\nThis list can contain anything, and will combine any elements of the same type.', sep='')                 # Prompt user to make a new list
    list1 = makeList()                                                                                                                          # Creates a list
    print('This list combines all similar elements in your list: ', (listCombine(list1)))                                                       # Calls and prints the return of listCombine
    
    print('Lets make our second list.\nThis list can contain anything, and will check to see if the list is sorted.')                           # Prompt user to make a new list
    list2 = makeList()                                                                                                                          # Creates a list
    if checkSorted(list2):                                                                                                                      # Calls checkSorted if check sorted returns true
        print('This list is sorted.')                                                                                                           # let user know the list is sorted
    else:                                                                                                                                       # else if check sorted returned false
        print('This list is not sorted.')                                                                                                       # let user know the list is not sorted
    
    print('Lets make our third list.\nThis list can contain only numbers, and will add all elements of the list.', sep='')                      # Prompt user to make a new list
    list3 = makeNumList()                                                                                                                       # Creates a list that only accepts numbers
    print('This is the sum of all elements in your list: ', (listSum(list3)))                                                                   # Calls and prints the return of listSum

    print('Lets make our fourth list.\nThis list can contain anything and will reverse the order of the list', sep='')                          # Prompt user to make a new list
    list4 = makeList()                                                                                                                          # Creates a list
    print('This is the reverse of your list: ', (listReverse(list4)))                                                                           # Calls and prints the return of listReverse
    
    print('Lets make two lists.\nThese lists can contain anything and will be sorted then combined.', sep='')                                   # Prompt user to make 2 new lists
    list5 = makeList()                                                                                                                          # Creates a list
    list6 = makeList()                                                                                                                          # Creates a list
    print('This is your two lists combined and sorted: ', (listSingleSorted(list5, list6)))                                                     # Calls and prints the return of listSingleSorted

    input('Press ENTER to Close Program')
main()
