"""
Syntax:
------------
for i in range(start, stop, step):
    # do something
"""

# for i in range(5):
#     print(i)

# print()

# for i in range(1,6):
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# for i in range(1,10,3):
#     print(i)

# for i in range(10,0,-2):
#     print(i)


# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

"""
4
43
432
4321
"""

for i in range(4,0,-1):
    for j in range(4,i-1,-1):
        print(j,end=" ")
    print()