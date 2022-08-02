"""
Tuple - immutable and Ordered
"""
mytuple = (12,32,"Royal",12.52)

print(type(mytuple))
print(mytuple)

# mytuple[2] = 12
print(mytuple)

tuple1 = 21,52,32,52,12

print(type(tuple1))
print(tuple1[0])

print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
print(sorted(tuple1))
print(sum(tuple1))

t1 = (89,)
print(type(t1))

print(tuple1.count(52))
print(tuple1.index(32))

"""
Unpacking of Tuple 
"""
t2 = ("apple","banana","cherry","Mango","berry","Orange")

# box1 , box2 , box3 = t2

# print(box1)
# print(box2)
# print(box3)


# box1 , box2 , *box3 = t2

# print(box1)  # First element
# print(box2)  # Second element
# print(box3)  # all other elements


# box1 , *box2 , box3 = t2

# print(box1)  # First element
# print(box2)  # all other elements
# print(box3)  # Last element


# *box1 , box2 , box3 = t2

# print(box1)  # all others element
# print(box2)  # Second last element
# print(box3)  # Last element

# t3 = (12,13,1,15)

# t3 = list(t3)

# t3.append(56)

# t3 = tuple(t3)
# print(t3)

"""
Take name as an input from the user.

Input:

Full name: Viha Anurag Shah

Output:

V.A.Shah
# """
# name = input("Enter Full name(firstname+Middlename+lastname):")
# print(name[0]+"."+name[name.index(" ")+1]+"."+name[name.rindex(" ")+1:])

# part1 = name[0]
# part2 = name[name.index(" ")+1]
# part3 = name[name.rindex(" ")+1:]

# print(part1+"."+part2+"."+part3)
"""
Write a program to find the number of vowels, consonents and white space characters in a given string.
Example:
input string: Python Programming
output:
vowels: 4
white spaces: 1
consonents: 13
"""