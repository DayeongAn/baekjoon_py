
#1
A = input().split()
if int(A[0]) > int(A[1]) :
    print(">")
elif int(A[0]) < int(A[1]):
    print("<")
else:
    print("==")
    
#2
    
Y = int(input(""))
if 1 <=  Y <= 4000:
    if Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0):
        print("1")
    else:
        print("0")

#3
        
        G = int(input(""))
if 90 <= G <= 100:    
    print("A")
elif 80 <= G <= 89:
    print("B")
elif 70 <= G <= 79:
    print("C")
elif 60 <= G <= 69:
    print("D")  
else:
    print("F")
