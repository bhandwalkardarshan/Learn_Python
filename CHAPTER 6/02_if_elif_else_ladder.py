# if elif else
a = int(input("enter your age: "))

if(a>18):
    print("you are eligible to vote")
elif(a<0):
    print("age must be +ve")
elif(a==0):
    print("age can't be zero")
else:
    print("you are not eligible to vote")

print("End of program")