# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

# read the file
with open("./donkey.txt", "r") as f:
    data = f.read()

data = data.replace("donkey", "#####")

# write the file
with open("./donkey.txt", "w") as f:
    f.write(data)