marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))
marks4 = int(input("Enter marks 4: "))

total_percentage = (marks1 + marks2 + marks3 + marks4) / 400 * 100

if(total_percentage >= 40 and marks1 >= 33 and marks2>=33 and marks3>=33 and marks4>=33):
    print("Pass")
else:
    print("Fail, try again")