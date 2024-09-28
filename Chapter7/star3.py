i = int(input("enter number: "))
n=1

while(n<=i):
    if(n == 1 or n ==i):
        print("*"*i)
    else:
        print("*",end="")
        print(" "*(i-2),end="")
        print("*",end="")
        print("")
    n +=1