
# a=input("Enter name:")
# print(a)
# def usd_to_inr():
#     usd=int(input("Enter amount to exchange(in Dollar)="))
#     inr=usd*80
#     print(f"Amount in INR={inr}")

# usd_to_inr()  
 
                      
#####Program to convert celsius into fahrenheit
def Cel_To_Fah(c):
 
    # Used the formula to convert temp
    return (c*1.8)+32
  
# Driver Code
# if __name__ == "__main__":
#   n = int(input("Enter temp in celsius:"))
 
#   # Function call
#   print("Temp in Fahrenheit:")
#   print(int(Cel_To_Fah(n)))
c=0
if -1000<=c<1000:
  c = int(input("Enter temp in celsius:"))
  print("Temp in Fahrenheit:")  
  print(int(Cel_To_Fah(c)))