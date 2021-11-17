'''
Write a script to concatenate N strings.
'''
N = int(input('enter the number of rows: '))
concatenated_string = ''
for _ in range(N):
    string = input('enter a string: ')
    concatenated_string += string
print(concatenated_string)