"""
Set is mutable and unordered collection of unique elements.
---> No duplicates
"""
# set1 = {12, 34, 56, 78, 90 , 12 , 34}
# print(set1)
# print(type(set1))
# print(len(set1))

# print(max(set1))
# print(min(set1))
# print(sum(set1))
# print(sorted(set1))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

set1.add(6)
print(set1)

set3 = set1.copy()
print(set3)

set4 = set1
print(set4)

set3.clear()
print(set3)

set1.discard(6)
print(set1)

print(set1.difference(set2))                                # set1 - set2 = {1,2,3,4,5} - {4,5,6,7,8} = {1,2,3}
# set1.difference_update(set2)
# print(set1)

print(set2.difference(set1))                           # set2 - set1 = {4,5,6,7,8} - {1,2,3} = {6,7,8}

print(set1.symmetric_difference(set2))                 # set1 - set2 = {1,2,3,4,5} - {4,5,6,7,8} = {1,2,3,6,7,8}

# set1.symmetric_difference_update(set2)
# print(set1)

print(set1.intersection(set2))

# set1.intersection_update(set2)
# print(set1)

set3 = {1,2,3}
set4 = {3,4,5}

print(set3.isdisjoint(set4))                   # True if no common elements in set3 and set4

set5 = {1,2,3,4,5}          

print(set5.issubset(set3))                 # True if set5 is subset of set3
print(set5.issuperset(set3))                # True if set5 is superset of set3

print(set3.pop())                       # Remove and return an element from set3
print(set3)

set3.remove(3)                       # Remove an element from set3
print(set3)

set5.discard(9)            # If not present, do nothing
print(set5)

# set5.remove(9)            # If not present, raise KeyError
# print(set5)

print(set1.union(set2))

set1.update(set2)
print(set1)

"""
Take a string from the user and take 3 characters also.

e.g.    HEllo! Good Morning How are you?

        char - "e" , "l" , "i"

Output: Good How you?
"""
input_str = input("Enter a string: ")

my_list = input_str.split(" ")

set1 = set()

for i in range(3):
    set1.add(input("Enter a character:"))

for i in my_list:
    for j in i:
        if j in set1:
            my_list.remove(i)
            break

print(str(my_list))

print(" ".join(my_list))