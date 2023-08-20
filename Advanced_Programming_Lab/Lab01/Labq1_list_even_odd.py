first_list = [int(x) for x in input("Enter numbers for the first list (separated by spaces): ").split()]
second_list = [int(x) for x in input("Enter numbers for the second list (separated by spaces): ").split()]
new_list = [x for x in first_list if x % 2 != 0] + [x for x in second_list if x % 2 == 0]
print("New list:", new_list)

