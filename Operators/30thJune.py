"""
Bitwise Operators
1) &
2) |
3) ^
4) <<
5) >>

Decimal to Binary:---->

2|45
2|22 --> 1
2|11 --> 0
2|5  --> 1
2|2  --> 1
 |1  --> 0 

45 --> 101101
43 --> 101011

1) & (and Operators)

a   b   a&b
0   0   0
0   1   0
1   0   0
1   1   1   

45 --> 1 0 1 1 0 1 
&      & & & & & &
43 --> 1 0 1 0 1 1 
------------------
       1 0 1 0 0 1 (41)
# """
# print(45&43)
# print(56&16)
# print(25&19)
"""
2) | (or Operators)

a   b   a&b
0   0   0
0   1   1
1   0   1
1   1   1   

45 --> 1 0 1 1 0 1 
|      | | | | | |
43 --> 1 0 1 0 1 1 
------------------
       1 0 1 1 1 1 (47)
# """
# print(45|43)
# print(56|16)
# print(25|19)

"""
3) ^ (Xor Operators)

a   b   a&b
0   0   0
0   1   1
1   0   1
1   1   0   

45 --> 1 0 1 1 0 1 
^      ^ ^ ^ ^ ^ ^
43 --> 1 0 1 0 1 1 
------------------
       0 0 0 1 1 0  (6)
# """
# print(45^43)
# print(56^16)
# print(25^19)

"""
4) SHIFT Operators

Types:--->
---------------

1) >>

43 -->  1 0 1 0 1 1

43<<2 --->
                    1   0   1   0   1   1   ---> 8
            32  16  8   4   2   1   
2) <<

43>>2 ---> 
            1   0   1   0   1   1   0   0   --->172
            128 64  32  16  8   4   2   1   
"""

# print(43<<2)
# print(43>>2)

# print(77<<5)    
# print(56>>4)
# print(35>>2)
# print(45<<3)

"""
Loops:-->

1) while
2) for

1) While loop:-->

initialization

while condition:
    //Logic codes
    increment/decrement
"""

i = 1

while i <= 5:
    print("Hello")
    i+=1      # i = i + 1 

"""
Task: 1) print 1 to n(user value)
      2) print n(user value) to 1 
"""