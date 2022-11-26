from copy import copy
from itertools import count


fruits=["apple","banana","cherry","orange"]
newList=[]
fruits.append("kiwi")
fruits.append("mango")

# print(f"Fresh List={fruits}")
# fruits[2]="papaya"
# print(f"after adding item={fruits}")
# fruits.remove(fruits[2])
# print(f"after removal={fruits}")

#---------------without comprehension---------------------------#
 
# for x in fruits:
#     if "a" in x:
#         newList.append(x)

# print(newList)
#----------------------------------------------------------------#

#----------------with comprehension------------------------------#
# newList=[x for x in fruits if "a" in x]
# print(f"NewList={newList}")
#----------------------------------------------------------------#

#-----------------copy list--------------------------------------#
# newList=copy(fruits)
# print(newList)
#             #------OR-------#
# newList=list(fruits)
# print(newList)
#----------------------------------------------------------------#

#----------------Join lists--------------------------------------#
L1=["a","b","c"]
L2=[1,2,3]
#         #using + operator
# L3=L1+L2
# print(f"method_1={L3}")
#         #using for loop
# for x in L2:
#     L1.append(x)
# print(f"method_2={L1}")
#         #using extend()
# L1.extend(L2)
# print(f"method_3={L1}")
L1.clear()
L1=copy(fruits)
print(f"L1={L1}")
cnt=L1.count("apple")
print(f"count={cnt}")
inx=L1.index("kiwi")
print(f"index={inx}")
L1.insert(4,"papaya")
print(L1)
L1.pop(4)       #removes last element as defaultif index isnt specified
print(L1)
L1.reverse()
print(L1)
L1.sort()
print(L1)
print(L1[-1])       #negative indexing