# sum of n natural numbers by recursion

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

num = int(input("Enter value of n: "))
print(f"Sum of first {num} natural numbers is", sum(num))