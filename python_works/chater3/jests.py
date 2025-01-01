jest = ['jet_ski', 'ufo',]
print(jest) # you can tag this out if you only want to see the chage without the old version of the list

jest[0] = 'space_ship'#we are changing the first item in the list to space_ship 
print(jest)

'''open
okay this is an example of modinfing a list is's simler to revoming a item from a list but instead of removing the item you are changing 
the item in the list and than repalcing it with a new item in the list

The code shown above is an example of modifying a list

 modifying the list is neither creating or adding an element to the list, it is simply changing the value of an element in the list

'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------#
jest = ['jet_ski', 'ufo',]
print(jest) 

jest.append('space_ship')#we are adding a new item to the list by using the append method
print(jest)

jest = []

jest.append('jet_ski')
jest.append('ufo')  
jest.append('space_ship')
print(jest)

'''open

okay pertymuch all what we did was that we added elemtns to the list by using the append method and we also created a empty list and than added
this is probably the most common way to build a list in python cuz we are probly not ging to know what the list is going to list at the start
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#instering elements into a list is more of an exstion of the append method but we can chage were we want to add the element in the list
jest = ['jet_ski', 'ufo',]

jest.insert(0, 'space_ship')#we are adding a new item to the list by using the insert method and becues it's 0 it will be the first iteam in the list.
print(jest) # rember that all the items in the list will be moved down by one index number thx '''ai for the help'''

jest = []

jest.insert(0,'jet_ski')
jest.insert(1,'ufo')  
jest.insert(2,'space_ship')
print(jest) #you can do this but it depending on your situation. like but must the itel have to be in a specific order or not ect.
#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#removing elements from a list
jest = ['jet_ski', 'ufo',]
print(jest)

del jest[1]# this is the del statement that is used to remove an item from a list once an item is removed from the list it is gone for good
print(jest)#we can't get it back unless we add it back to the list

jest = ['jet_ski', 'ufo',]
print(jest)

del jest[-1]
print(jest)
#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#the .pop() method is once aging like an exsteion of the .remmove methor but this time we can remove the last item in the list
jest = ['jet_ski', 'ufo',]
print(jest)

pop_jest = jest.pop()#this is the pop method that is used to remove the last item in the list and it also returns the item that was removed
print(jest)#we can't get it back unless we add it back to the list
print(pop_jest)#this is the item that was removed from the list and it is stored in the pop_jest variable thuss we can still ues it in the code
#----------------------------------------------------------------------------------------------------------------------------------------------------------#
#removing an item from a list by value, how is this diffrent from the other methods or the .remove() method
jest = ['jet_ski', 'ufo',]
print(jest)

jest.remove('ufo')#this is the remove method that is used to remove an item from the list by value
print(jest) 


jest = ['jet_ski', 'ufo',]
print(jest)

to_expensive = 'ufo'#this is the item that we want to remove from the list and we are storing it in a variable
jest.remove(to_expensive) #we are removing the item from the list by value
print(jest)#this is the list after the item is removed from the list
print(f"\nA {to_expensive.title()} is to expensive for me.")#this is a message that is printed out after the item is removed from the list
#----------------------------------------------------------------------------------------------------------------------------------------------------------#

'''
So we lerna about list and how we can removew, add, and modify the list and we also learned about the .pop() method that is used to remove the last item in the list
and we also learned about the .remove() method that is used to remove an item from the list by value 
and we also learned about the del statement that is used to remove

evem though they do dfiffent thans they all have the same goal and that is to remove an item from the list or to change it's value in someway
coding is like a par of wings it give you the ability to fly and to see the world in a diffrent way your main 
is what liment you and what you can do with the wings that you have.

1/1/2025 6:42PM age 13
'''