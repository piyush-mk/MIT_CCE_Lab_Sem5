def list_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def main():
    lst = []
    while True:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0: break
        lst.append(num)
    result = list_product(lst)
    print(result)
main()
