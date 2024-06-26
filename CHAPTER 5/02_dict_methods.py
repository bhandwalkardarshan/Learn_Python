marks = {
    "key":"value",
    "darshan":68,
    "rohan":45
}

# print
print(marks["darshan"])

print(marks.items())

print(marks.keys())

print(marks.values())

# updation
# marks["darshan"] = 90
marks.update({"kavi":95, "praj":80})
print(marks)

# getting values
print(marks.get("kavi2"))   # returns "None"
# print(marks["kavi2"])       # returns error

# deletion
marks.pop("darshan")
print(marks)

marks.popitem() #removes last entry
print(marks)