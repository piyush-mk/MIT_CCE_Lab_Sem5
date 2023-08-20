def uniquer(lst):
    print(set(lst))

input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [item for item in input_str.split()]
uniquer(input_list)
