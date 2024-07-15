# sum of n natural  numbers

n = int(input("Enter the number: "))
sum = 0
i = 1
while(i<=n):
    sum = sum + i
    i = i + 1

print("sum of natural numbers upto n: ",sum)