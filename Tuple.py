T1=("apple","banana","kivi","mango","orange")
T2=(1,2,3,4,5)

#Access Tuple items
print(T1[-1],T2[3])

#updating elements of tuple: assigning direct value 
if "kivi" in T1:
    L1=list(T1)
    L1[2]="kiwi"
    T1=tuple(L1)
    print(f"T1={T1}")

#updating elements of tuple: using append method
L2=list(T2)
L2.append(6)

#Remove item from tuple
L2.remove(1)
T2=tuple(L2)
print(f"T2={T2}")

#combining tuples
print(T1+T2)

#Completely delete tuple
#del T2
print(f"T2={T2} no more exists")

#unpacking tuple
print(f"T1={T1}")
(a,*b,c)=T1
print(a,b)
print(b)
print(c)

