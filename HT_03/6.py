'''
6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
'''
import random


st = 'f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345'
lst = random.sample(list(st), random.randint(20, 60))
string = ''.join(lst)

def if_the_length_of_the_string(s):
    string_of_letters = ''.join(list(filter(lambda x: x.isalpha(), s)))
    string_of_numbers = ''.join(list(filter(lambda x: x.isdigit(), s)))
    sum_string_of_numbers = sum(list(map(int, string_of_numbers)))
    if 30 <= len(s) <= 50:
        print('len s', len(s))
        print('len string_of_letters', len(string_of_letters))
        print('len string_of_numbers', len(string_of_numbers))
    elif len(s) < 30:
        print('sum_string_of_numbers', sum_string_of_numbers)
        print('string_of_letters', string_of_letters)
    elif len(s) > 50:
        print('string_of_letters', string_of_letters)
        print('string_of_numbers', string_of_numbers)

if_the_length_of_the_string(string)