i = int(input("enter number to print series sum :"))
sum=1
x=0
for x in range(i+1):
    sum = x+sum
    x +=1
    print(sum)

print(f'Final result {sum}')