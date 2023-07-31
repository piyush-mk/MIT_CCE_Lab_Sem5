
n = int(input("Enter the number of strings: "))
strings_list = []
for i in range(n):
    string = input(f"Enter string {i+1}: ")
    strings_list.append(string)
print("The strings you entered are:")
print(strings_list)


count = 0
for string in strings_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
        
print("number of strings with the same first and last character and length 2 or more is: ",count)
print("odd len strings: ")
for string in strings_list:
    if len(string)%2!=0:
        print(string)