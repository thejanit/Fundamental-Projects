user_input = input("Enter the Phrase: ").split()
a = ''
for i in user_input:
    a = i[0].upper()
    print(a, end='')