def main():
    lst = []
    while True:
        num = int(input("Enter a number (-9999): "))
        if num == -9999: break
        lst.append(num)
    uniquer(lst)

def uniquer(lst):
    print(set(lst))
main()