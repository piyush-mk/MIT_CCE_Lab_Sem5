def multiply_list_numbers(lst):
    result = 1
    for num in lst:
        if isinstance(num, (int, float)):
            result *= num
    return result

input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [float(item) for item in input_str.split()]

output = multiply_list_numbers(input_list)
print("Output:", output)