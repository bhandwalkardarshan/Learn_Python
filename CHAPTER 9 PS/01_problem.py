f = open("./CHAPTER 9 PS/poems.txt")
content = f.read()

if("twinkle" in content):
    print("twinkle is in the poem")
else:
    print("twinkle is not in the poem")

f.close()
