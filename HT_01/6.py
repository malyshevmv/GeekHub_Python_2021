'''
Write a script to check whether a specified value is contained in a group of values.
        Test Data :
        3 -> [1, 5, 8, 3] : True
        -1 -> (1, 5, 8, 3) : False
'''
value = input('enter a value: ')
group_of_values = list(map(str, input('enter a value through the space bar').split()))
flag = 0
if group_of_values.count(value):
    flag = True
else:
    flag =  False
print(f'{value} -> {group_of_values}: {flag}')