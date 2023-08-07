count = {}
sent = input("Enter a Line : ")
list_of_words = sent.split()
for word in list_of_words:
    count[word] = count.get(word, 0) + 1
print('Frequency')
for key in count.keys():
    print(key, count[key])
