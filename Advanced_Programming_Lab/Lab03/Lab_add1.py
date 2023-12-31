def count_upper_lower_characters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

sample_string = input("Enter a string: ")
upper_count, lower_count = count_upper_lower_characters(sample_string)
print(f"No. of Upper case characters: {upper_count}")
print(f"No. of Lower case characters: {lower_count}")
