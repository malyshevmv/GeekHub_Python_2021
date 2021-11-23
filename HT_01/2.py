'''
2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.
        Test Data :
        color_list_1 = set(["White", "Black", "Red"])
        color_list_2 = set(["Red", "Green"])
        Expected Output :
        {'Black', 'White'}
'''
color_list_1 = map(str, input('enter a comma-separated color for list_1: ').split(', '))
color_list_2 = map(str, input('enter a comma-separated color for list_2: ').split(', '))
print(set(color_list_1) - set(color_list_2))