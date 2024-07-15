# degree celcius

def f_to_c(f):
    c = (f - 32) * 5 / 9
    return c

f = int(input("Enter temperature in F: "))
print("Tempearature in Degree Celcius:",round(f_to_c(f),2))