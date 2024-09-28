def factorial(n):
    if(n==0 or n==1):
        res = 1
    else:
        res = n*factorial(n-1)
    return res

n = int(input("Enter number to calculate factorial: "))
res = factorial(n)
print(res)