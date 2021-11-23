'''
Write a script to convert decimal to hexadecimal
        Sample decimal number: 30, 4
        Expected output: 1e, 04
'''
numbers_10 = list(map(int, input('enter numbers separated by a space').split()))
numbers_16 = []
for i in numbers_10:
    numbers_16.append(hex(i)[2:])
print(*numbers_16)