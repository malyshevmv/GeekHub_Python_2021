'''
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......
'''
def traffic_lights():
    import time

    kolir_dlya_avto = [
        'Red',
        'Red',
        'Red',
        'Red',
        'Yellow',
        'Yellow',
        'Green',
        'Green',
        'Green',
        'Green',
        'Yellow',
        'Yellow'
    ]
    kolir_dlya_pishohoda = [
        'Green',
        'Green',
        'Green',
        'Green',
        'Green',
        'Green',
        'Red',
        'Red',
        'Red',
        'Red',
        'Red',
        'Red'
    ]
    while True:
        for sv_avt, sv_pish in zip(kolir_dlya_avto, kolir_dlya_pishohoda):
            time.sleep(1)
            print(sv_avt, '\t', sv_pish)

traffic_lights()
