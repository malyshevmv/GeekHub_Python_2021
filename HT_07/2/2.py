'''
2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
   Кількість символів в блоках - та, яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі
   (наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
   В репозиторій додайте і ті файли, по яким робили тести.
   Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл,
   а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість.
   В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
   Наприклад:
   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
                     ⏫ центр
   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно
                     ⏫ центр
'''

def function(file, number_of_characters):
    with open(file) as f:
        data_f = f.read()
        if (len(data_f) // 3) <= number_of_characters:
            return 'invalid values entered'
    if len(data_f) % 2 != 0 and number_of_characters % 2 != 0:
        kilkist_probiliv = (len(data_f) - 3*number_of_characters) // 2
        center = data_f[number_of_characters + kilkist_probiliv:number_of_characters + kilkist_probiliv + number_of_characters]
        return f'{data_f[:number_of_characters]}{" "*kilkist_probiliv}{center}{" "*kilkist_probiliv}{data_f[-number_of_characters:]}'
    elif len(data_f) % 2 == 0 and number_of_characters % 2 == 0:
        kilkist_probiliv = (len(data_f) - 3*number_of_characters) // 2
        center = data_f[number_of_characters + kilkist_probiliv:number_of_characters + kilkist_probiliv + number_of_characters]
        return f'{data_f[:number_of_characters]}{" "*kilkist_probiliv}{center}{" "*kilkist_probiliv}{data_f[-number_of_characters:]}'
    else:
        if len(data_f) % 2 != 0 and number_of_characters % 2 == 0:
            data_f = data_f[:-1]
            kilkist_probiliv = (len(data_f) - 3*number_of_characters) // 2
            center = data_f[number_of_characters + kilkist_probiliv:number_of_characters + kilkist_probiliv + number_of_characters]
            return f'{data_f[:number_of_characters]}{" "*kilkist_probiliv}{center}{" "*kilkist_probiliv}{data_f[-number_of_characters:]}'
        elif len(data_f) % 2 == 0 and number_of_characters % 2 != 0:
            kilkist_probiliv = (len(data_f) - 3*number_of_characters) // 2
            center = data_f[number_of_characters + kilkist_probiliv:number_of_characters + kilkist_probiliv + number_of_characters]
            return f'{data_f[:number_of_characters]}{" "*kilkist_probiliv}{center}{" "*kilkist_probiliv}{data_f[-number_of_characters:]}'

print(function('test0.txt', 2))