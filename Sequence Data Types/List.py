"""
List is mutable sequence data type.
List is a collection of items in a particular order.
# """
# myList = [12,"Hello",True,12.52,2+5j]

# print(myList)

"""
Positive Index:

12          0
Hello       1
True        2
12.52       3
(2+5j)      4
# """
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])
# print(myList[5])

"""
Negative Index:
12        -5
Hello     -4
True      -3
12.52     -2
(2+5j)    -1
# """
# print(type(myList))
# print(len(myList))
# print(max(myList))

# list1 = [1,2,34,54,76,89,12,76,23,21,12,1]

# print(len(list1))
# print(max(list1))
# print(min(list1))
# print(sum(list1))
# print(sorted(list1))
# print(sorted(list1,reverse=True))

# list2 = ["Apple","apple","banana","cherry","mango","ball"]

# print(max(list2))
# print(min(list2))
# print(sorted(list2))
# print(sorted(list2,reverse=True))

# print(list2)

# for i in list2:
#     print(type(i))
#     print(i)

"""
Take list with 10 elements and find out maximum, minimum , sum and average of the list.
"""

myList = [1,2,3,4,5,6,7,8,9,10]
# print(myList)

# myList.append(11)   # Append element to the end of the list

# print(myList)

# myList.append(int(input("Enter the element to be appended: ")))
# print(myList)

# list1 = []

# for i in range(10):
#     list1.append(int(input("Enter the element to be appended: ")))

# print(list1)

"""
Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
"""
myList = [1,2,3,4,5,6,7,8,9,10]

List2 = myList.copy()

print(List2)

List3 = myList
print(List3)

print(id(myList))
print(id(List2))
print(id(List3))

print(myList is List2)
print(myList is List3)

List2.clear()
print(List2)

del List2
# print(List3)

print(myList.count(1))

myList.extend([11,12,13,14,15])
print(myList)

print(myList.index(11))

myList.insert(2,22)
print(myList)

myList.pop(2)
print(myList)

myList.remove(11)
print(myList)

myList.reverse()
print(myList)

myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)

"""
list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    
"""