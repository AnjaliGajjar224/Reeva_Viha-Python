# """
# Dictionaries are immutable and unordered.
# ---> Dictionary are key-value pairs
# """
# myDict = {
#     "a":"apple",
#     "b":"banana",
#     "c":"cherry",
#     "m":"mango"
# }

# print("Type of the Variable myDict: ",type(myDict))

# # set1 = set()
# # print(type(set1))

# print(myDict["a"])
# print(myDict["b"])         # banana
# print(myDict["c"])
# print(myDict["m"])

# dict1 = myDict.copy()
# print(dict1)

# dict1.clear()
# print(dict1)

# # del dict1
# # print(dict1)

# x = "key1","key2","key3"
# y = 0,1,2

# print(dict1.fromkeys(x,y))

# print(myDict.get("a"))

# print(myDict.items())           # items contains keys and values

# print(myDict.keys())

# print(myDict.values())

# print(myDict.pop("m"))
# print(myDict)

# print(myDict.popitem())
# print(myDict)

# print(myDict.setdefault("e","blueberry"))
# print(myDict)

# print(myDict.setdefault("a","mango"))
# print(myDict)

# print(myDict.update({'a':'mango'}))
# print(myDict)

# print(myDict.values())

# for i in myDict.values():
#     print(i)


# child1 = {
#     1 : "John",
#     2 : "Michel",
#     3 : "Smith"
# }


# child2 = {
#     "@":"Jack",
#     "&":"Hi"
# }

# child3 = {
#     1.5: 12,
#     2.5: 13

# }

# parent = {
#     1 : child1,
#     2 : child2,
#     3: child3 
# }

# print(parent)

# print(parent.get(1))