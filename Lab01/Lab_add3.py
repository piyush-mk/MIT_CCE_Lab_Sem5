s=input("enter string: ")
try:
    int(s, 16)
    print(s, "is a hexadecimal no.")
except ValueError:
    print(s, "is not a hexadecimal no.")
