"""
6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
"""


class Counter(object):
    counter = 0

    def __init__(self):
        self.__class__.counter += 1


a = Counter()
b = Counter()
c = Counter()
d = Counter()
print(Counter.counter)
