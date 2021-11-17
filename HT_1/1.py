'''
1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
        Sample data : 1, 5, 7, 23
        Output :
        List : [‘1', ' 5', ' 7', ' 23']
        Tuple : (‘1', ' 5', ' 7', ' 23')
'''
numbers = map(str, input('enter a sequence of numbers separated by commas: ').split(', '))
lst_numbers = list(numbers)
print(f'List: {lst_numbers}')
print(f'Tuple: {tuple(lst_numbers)}')