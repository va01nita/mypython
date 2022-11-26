from itertools import count
from operator import index


T1=("apple","banana","kivi","mango","orange")
T2=(1,2,3,4,5)

no = input(
    "1 For Access Tuple items\n"
    "2 For updating elements of tuple: assigning direct value\n"
    "3 For updating elements of tuple: using append method\n"
    "4 for Loop in Tuple\n"
    "5 while loop in Tuple\n"
    "6 Join Tuples\n"
    "7 Tuple Methods\n"
    )

match no:
    case "1":        
        print(
            f"T1={T1}\n"
            f"T2={T2}"
            )
        print(
            f"Access Tuple items at T1[-1] ={T1[-1]}\n",
            f"Access Tuple items at T1[1] ={T1[1]}\n",
            f"Access Tuple items at T1[4] ={T1[4]}\n",
            f"Access Tuple items at T1[0:] ={T1[0:]}\n",
            f"Access Tuple items at T1[1:] ={T1[1:]}\n",
            f"Access Tuple items at T1[:1] ={T1[:1]}\n",
            f"Access Tuple items at T1[0:4] ={T1[0:4]}\n",
            f"Access Tuple items at T1[2:4] ={T1[2:4]}\n",
            
            
            )
    case "2":
        print(
            f"T1={T1}\n"
            f"T2={T2}"
            )
        if "kivi" in T1:
            L1=list(T1)
            L1[2]="kiwi"
            T1=tuple(L1)
            print(f"T1={T1}")
    case "3":
        print(
            f"T1={T1}\n"
            f"T2={T2}"
            )
        L2=list(T2)
        L2.append(6)
        T2 = tuple(L2)
        print(T2)
    
    case "4": #for loop to access Tuple
        print(
            f"T1={T1}\n"
            f"T2={T2}"
            )
        for x in range(len(T1)):
         print(x)
        print (T1[-3])

    case "5":#while loop to access tuple
        print(
            f"T1={T1}\n"
            f"T2={T2}"
            )
        i=0
        while i<len(T1):
            print(T1[i])
            i=i+1 

    case"6":# Join tuples by adding and multyplying
        print(
            f"T1={T1}\n"
            f"T2={T2}"
            )
        ComnT =T1+T2
        print(f"Added Tuples:{ComnT}\n")
        myTuple= T2*2
        print(f"Multiplied by 2:{myTuple}\n")   
    
    case "7":#Tuple methods
        print(
            f"T1={T1}\n"
            f"T2={T2}"
            )
        
        cnt= T2.count("6")
        print(f"count of 6 in T2:{cnt}")
        indx= T1.index("kivi")
        print(f"Index of kivi in T1:{indx}")



    case _:
        print("0")