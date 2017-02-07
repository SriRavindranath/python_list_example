# empty list
my_list = []

print my_list

# list of integers
my_list = [1, 2, 3]
print my_list

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
print my_list

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
print my_list


/////////////// LIST INDEXING////////////
my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])

# Output: o
print(my_list[2])

# Output: e
print(my_list[4])

# Error! Only integer can be used for indexing
# my_list[4.0]

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Output: a
print(n_list[0][1])    

# Output: 5
print(n_list[1][3])

///////////////NEGATIVE INDEXING /////////////////////

my_list = ['p','r','o','b','e']

# Output: e
print(my_list[-1])

# Output: p
print(my_list[-5])

//////////////////////SLICING A LIST ///////////////////

my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

///////////// ADDING or CHANGING THE ELEMNETS in THE LIST //////////

# mistake values
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

# Output: [1, 4, 6, 8]
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

# Output: [1, 3, 5, 7]
print(odd) 

//////////////////// APPEND AND EXTEND FUNCTION //////////

odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)



//////////////////USING + and * ////////////////////

odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]
print(["re"] * 3)

////////////// INSERT METHOD //////////// for Specific location in the list

odd = [1, 9]
odd.insert(1,3)

# Output: [1, 3, 9] 
print(odd)

odd[2:2] = [5, 7]

# Output: [1, 3, 5, 7, 9]
print(odd)

///////////////////// DELETE or REMOVE elements from the list/////////

my_list = ['p','r','o','b','l','e','m']

# delete one item
del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)

# delete multiple items
del my_list[1:5]  

# Output: ['p', 'm']
print(my_list)

# delete entire list
del my_list       

# Error: List not defined
print(my_list)

/////////////// USing REMOVE(), POP(), clear()//////////////

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)


////////////// deleting a list item by assigning a empty list to it/////////////

Python console output below.
>>> my_list = ['p','r','o','b','l','e','m']
>>> my_list[2:3] = []
>>> my_list
['p', 'r', 'b', 'l', 'e', 'm']
>>> my_list[2:5] = []
>>> my_list
['p', 'r', 'm']


/////////PYTHON LIST METHODS/////////////


Python List Methods
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list





///////SOME EXAMPLE OF PYTHON LIST method use cases/////////

my_list = [3, 8, 1, 6, 0, 8, 4]

# Output: 1
print(my_list.index(8))

# Output: 2
print(my_list.count(8))

my_list.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)

my_list.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)


//////////////// BEST PRACTISES /////////////
below methods/type is best and elegant way of programming
pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

Instead of the below code.

pow2 = []
for x in range(10):
   pow2.append(2 ** x)


/////////////List membership test/////////////

my_list = ['p','r','o','b','l','e','m']

# Output: True
print('p' in my_list)

# Output: False
print('a' in my_list)

# Output: True
print('c' not in my_list)

////////////////////


QUestions for YOu

#! /bin/python

for fruit in ['apple','banana','mango']:
    print("I like",fruit)
    
what will be the output??????   


