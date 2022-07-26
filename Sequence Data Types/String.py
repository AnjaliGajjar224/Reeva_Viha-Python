"""
Sequence Data Types
1) String
2) List
3) Tuple
"""
"""
String is ordered and immutable sequence of characters.
"""
# ch = 'a'

# print(type(ch))
# print(ch)

# myStr = "Python"
# print(myStr)

"""
    Positive Indexing
P       0
y       1
t       2
h       3
o       4
n       5
"""

# print("Length of the String: ",len(myStr))
# print("First Character: ",myStr[0])
# print(myStr[1])
# print(myStr[2])
# print(myStr[3])
# print(myStr[4])
# print(myStr[5])
# print(myStr[6])

"""
    Negative Indexing
P       -6
y       -5
t       -4
h       -3
o       -2
n       -1
"""

# print("Last Character: ",myStr[-1])
# print("Second Last Character: ",myStr[-2])
# print("Third Last Character: ",myStr[-3])
# print("Fourth Last Character: ",myStr[-4])
# print("Fifth Last Character: ",myStr[-5])
# print("Sixth Last Character: ",myStr[-6])

# print("Seventh Last Character: ",myStr[-7])

"""
Take a String and print the character at the specified index.
"""

# my_Str = input("Enter a String: ")
# index = int(input("Enter the index: "))

# print("Character at index: ",my_Str[index])

"""
Slicing a String 
------------------
1) [start:end]
2) [start:end:step]
3) [start:]
4) [:end]
5) [:]
"""

# myStr = "Python is a Programming Language"

# print(myStr)
# print("Length of the String:",len(myStr))
# print(myStr[12])
# print(myStr[2:12])

# print(myStr[0:16])

# print(myStr[-19:-1])

# print(myStr[:])

# print(myStr[5:])

# print(myStr[:20])

# print(myStr[-20:])

# print(myStr[:-26])

# print(myStr[::1])

# print(myStr[::2])

# print(myStr[10:30])
# print(myStr[10:30:3])

# print(myStr[-31:-5])
# print(myStr[-31:-5:2])
               
# print(myStr[-1:-19])
# print(myStr[30:16])

# print(myStr[-1:-19:-1])
# print(myStr[30:16:-1])

# print(myStr[::-1])
# print(myStr[::-2])

# print(myStr)

"""
Take a string from the user, Take a starting index from the user, Take an ending index from the user, Take a step size from the user.Then Print the characters from the starting index to the ending index in the specified step size.
"""

# my_Str = "royal_Technosoft_Pvt_Ltd."

# print(len(my_Str))
# print(my_Str.center(5))

# print(my_Str.center(50))          # 50 - length of the string = 50 - 25 = 25 spaces on both sides

# print(my_Str.center(51,"*"))

# print(my_Str.capitalize())

# print(my_Str.casefold())

# print(my_Str.count("o"))
# print(my_Str.count("o",0,10))

# print(my_Str.encode())        # Encodes the string into UTF - 8 format

# print(my_Str.endswith("Ltd."))
# print(my_Str.endswith("Ltd"))

# text = "Python\tis\ta\tProgramming\tLanguage"

# print(text)
# print(text.expandtabs(20))

# my_str = "Python is a Programming Language"

# print(my_str.find("o"))
# print(my_str.find("o",5,15))
# print(my_str.rfind("o"))

num1 = 15
num2 = 10

print(num1,"+",num2,"=",num1+num2)

print(f"{num1} + {num2} = {num1+num2}")

print("Your age is {age}".format(age=25))

my_str = "Python is a Programming Language"

print(my_str.index("Python"))
print(my_str.rindex("o"))

print(my_str.find("b"))                  # Returns -1 if not found
# print(my_str.index("b"))                 # Raises an error if not found

print("ABC123".isalnum())           # Returns True if all characters are alphanumeric
print("123".isalnum())
print("ABC".isalnum())  
print("$&ABCS!!".isalnum())

print("ABCD".isalpha())         # Returns True if all characters are alphabets
print("123".isdecimal())        # Returns True if all characters are digits ( 0 to 9 )

# print("6.9".isdecimal())

s5 = "2022"
print(s5.isdecimal())   # considers strictly plain digits from 0 to 9 only, nothing else
print(s5.isdigit())     # considers subscripts, superscripts and circled numbers also as numbers
print(s5.isnumeric())   # considers vulgar fractions, roman numerals, numbers from other languages
s6 = "2⁸"
print(s6)
print(s6.isdecimal())
print(s6.isdigit())
print(s6.isnumeric())

s7 = "②⓪②②"
print(s7)
print(s7.isdecimal())
print(s7.isdigit())
print(s7.isnumeric())
s8 = "¼"
print(s8)
print(s8.isdecimal())
print(s8.isdigit())
print(s8.isnumeric())
s9 = "二千二十二"
print(s9)
print(s9.isdecimal())
print(s9.isdigit())
print(s9.isnumeric())
s10 = "IV"
s11 = "Ⅵ"
print(s10)
print(s10.isnumeric())
print(s11)
print(s11.isnumeric())

my_str = "Python is a Programming Language"
str1 = "python is a fun"
print(my_str.istitle())
print(my_str.title())

print(str1.islower())
print(my_str.lower())

print(str1.isupper())
print(str1.upper())

print("  ".isspace())
print("      Hey     ".isspace())

print("\t".isspace())

print("\n".isspace())

print("&num1".isidentifier())
print("num1".isidentifier())
print("123num1".isidentifier())

s1 = "Goood Morning"
s2 = "Hello"

print(s1.join(s2))
print(s1.ljust(20,"*"))
print(s1.rjust(20,"*"))

print(s1.ljust(20))
print(s1.rjust(20))

print("$$$$$$$$$$Hey".lstrip("$"))
print("Hey$$$$$$$$$$".rstrip("$"))
print("$$$$$$$$$$$$Hey$$$$$$$$$$$".strip("$"))

print("Hello World".partition("o"))
print("Hello World".rpartition("o"))

print("Hello World".split("o"))
print("Hello World".rsplit("o"))

print("Hello\nWorld\nGood\nMorning".splitlines())

print("Helllo".replace("o","u"))

print("Hello World".startswith("H"))

print("Hello".swapcase())

text = "1-12-2022"

print(text.zfill(10))

text = "Hey"
print(text.zfill(10))
