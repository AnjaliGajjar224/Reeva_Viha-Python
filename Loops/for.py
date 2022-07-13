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

# for i in range(4,0,-1):
#     for j in range(4,i-1,-1):
#         print(j,end=" ")
#     print()

"""
54321
4321
321
21
1
# """
# n = int(input("Enter the number of rows: "))  
# for i in range(0, n + 1):    
#     for j in range(n- i, 0, -1):  
#         print(j, end=' ')  
#     print()  

"""
Task  : 12345
         1234
          123
           12
            1

"""
# n = int(input("Enter n : "))

# for i in  range (1, n +1):
#     k = 1
#     for j in range(1 , n+1):
#         if j<i:
#             print(" ",end = "")
#         else:
#             print(k , end = "")
#             k += 1
#     print()


"""
for..else
# """
# for i in range(5):
#     print(i)
# else:
#     print("Number is no longer in range")

"""
break: ---> breaks out of the loop
continue: ---> skips the current iteration of the loop
"""

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Number is equal to 3")


for i in range(5):
    if i == 3:
        continue
    print(i)