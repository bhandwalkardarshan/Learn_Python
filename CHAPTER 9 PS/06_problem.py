# Write a program to mine a log file and find out whether it contains ‘python’.
# If it does, print the line number and the line itself.

filepath = "log.txt"
with open(filepath, 'r') as file:
    data = file.read()
    if "python" in data:
        print("Line number: ", data.index("python"))
        print("Line: ", data[data.index("python"):data.index("python")+100])
    else:
        print("No ""python"" found in the file")