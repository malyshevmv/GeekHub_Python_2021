'''
Write a script to sum of the first n positive integers.
'''
number = int(input('enter an integer, a natural number: '))
total = 0
for i in range(1, number + 1):
    total += i
print(total)