import random

def is_special_string(s):
    return all(c.isalnum() == False for c in s)

def main():
    n = int(input("Enter the number of dictionary items: "))
    my_dict = {}

    for _ in range(n):
        key = random.randrange(0, 100)
        value = input(f"Enter a value for key {key}: ")
        my_dict[key] = value

    print("Dictionary:", my_dict)

    values = list(my_dict.values())

    total = 0
    numeric_count = 0
    string_concat = ""
    string_values = []

    for value in values:
        if value.isdigit():
            total += int(value)
            numeric_count += 1
        else:
            string_concat += value + " "
            string_values.append(value)

    if numeric_count > 0:
        average = total / numeric_count
        print(f"Average of numeric values: {average:.2f}")

    if string_values:
        print(f"Concatenated string values: {string_concat.strip()}")

    search_value = input("Enter a string value to search for in the dictionary: ")
    found_keys = [key for key, value in my_dict.items() if value == search_value]
    if found_keys:
        print(f"Keys associated with the search value '{search_value}': {found_keys}")
    else:
        print(f"No keys found for the search value '{search_value}'")

    special_string_values = [value for value in string_values if is_special_string(value)]
    if special_string_values:
        print("String values with only special characters:", special_string_values)
    else:
        print("No string values with only special characters found")

if __name__ == "__main__":
    main()
