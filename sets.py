mySet={"apple","banana","cherry","orange"}
print(mySet)

no = input(
    "1 Duplicate values are not allowed\n"
    "2 Getting length of sets\n"
    "3 Data types in sets\n"
    "4 type() method to get the type of sets\n"
    "5 Access set items\n"
    "6 Add set items using add()method\n"
    "7 Add any iterable such as set/list/tuple to sets using update()method\n"
    "8 Remove set items using remove() method\n"
    "9 Remove set items using discard() method\n"
    "10 Remove set items using pop() method\n"
    "11 Join sets using union()\n"
    "12 Join sets using update()\n"
    "13 Intersection_update()\n"
    "14 intersection()\n"
    "15 symmetric_difference_update()\n"
    "16 symmetric_difference\n"
)

match no:
    case "1":#duplicate values arennot allowed
        newSet={1,2,3,4,1,2}
        print(f"Duplicate values are removed:{newSet}")
    
    case "2":
        print(mySet)
        lenth=len(mySet)
        print(f"Lenth={lenth}")
        
    case "3":
        theSet={"a",1,2.0,True}
        print(f"sets can be of anytype={theSet}") 

    case "4":
        print(mySet)
        print(f"The type() method returns:{type(mySet)}")

    case "5":
        print(mySet)
        for x in mySet:
            print(x)
    
    case "6":
        print(f"mySet={mySet}")
        mySet.add("mango")
        print(f"After adding new item:{mySet}")

    case "7":
        print(mySet)
        L1=["papaya","kiwi"] #sets/tuples/dictionaries can also be added using update() method
        mySet.update(L1)
        print(f"After adding List:{mySet}")

    case "8":
        print(mySet)
        mySet.remove("apple")
        print(f"After removal={mySet}")
    
    case "9":
        print(mySet)
        mySet.discard("mango")
        print(f"After Removal={mySet} OR item does not exists")    

    case "10":
        print(mySet)
        mySet.pop()
        print(f"After Removal={mySet}")

    case "11":
        s1={1,2,3,4,5}
        s2={6,7,8,9,10}
        print(f"s1+s2={s1.union(s2)}") 

    case "12":   
        s1={1,2,3,4,5}
        s2={6,7,8,1,2}
        s1.update(s2)
        print(f"s1={s1}")

    case "13":
        s1={1,2,3,4,5}
        s2={6,7,8,1,2}
        s1.intersection_update(s2)
        print(f"s1={s1}")

    case "14":
        s1={1,2,3,4,5}
        s2={6,7,8,1,2}
        s3=s1.intersection(s2)
        print(f"s3={s3}")

    case "15":
        s1={1,2,3,4,5}
        s2={6,7,8,1,2}
        s1.symmetric_difference_update(s2)
        print(f"s1={s1}")

    case "16":
        s1={1,2,3,4,5}
        s2={6,7,8,1,2}
        s3=s1.symmetric_difference(s2)
        print(f"s3={s3}")

 

    case _:
        print("null")

    
        

