n = int(input("Enter number to print stars:"))

i = 1
s=1
for i in range(1,n+1):
    print(" "*(n-1),end="")
    n -=1
    print("*"*((2*i)-1),end="")
    print(" ")


