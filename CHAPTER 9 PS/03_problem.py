# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

import os

def generateTable(n):
    # Create the directory if it doesn't exist
    os.makedirs("./13-year-old", exist_ok=True)
    
    # Create the file path
    file_path = f"./13-year-old/{n}th table.txt"

    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(file_path, "w") as file:
        file.write(table)

for i in range(2,21):
    generateTable(i)
    
print("Tables generated!!!")

