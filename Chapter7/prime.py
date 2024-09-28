i = int(input("enter number to check if prime :"))
x = 2
for x in range(2,i):
    if((i%x) == 0):
        print("Not prime")
        break
    x+=1
else:
    print("prime")


