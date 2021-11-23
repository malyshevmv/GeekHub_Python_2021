'''
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
'''
def season(number_of_the_month: int):
    if 1 <= number_of_the_month <= 2 or number_of_the_month == 12:
        return 'Зима'
    elif 3 <= number_of_the_month <= 5:
        return 'Весна'
    elif 6 <= number_of_the_month <= 8:
        return 'Літо'
    elif 9 <= number_of_the_month <= 11:
        return 'Осінь'
    else:
        return 'sorry, but you did not enter a number from 1 to 12'


for i in range(13):
    print(season(i))