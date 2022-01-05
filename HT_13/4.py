"""
4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури
при створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
"""


class Figure(object):

    def __init__(self, color):
        self.color = color

    def change_the_color_of_the_figure(self, color_figure):
        self.color = color_figure


class Oval(Figure):
    def __init__(self, circuit, color):
        super(Oval, self).__init__(color)
        self.circuit = circuit


class Square(Figure):
    def __init__(self, length_square, color):
        super(Square, self).__init__(color)
        self.length_square = length_square


ab = Square(1, 'while')
ac = Oval(2, 'black')

for k, v in ab.__dict__.items():
    print(k, v)
print()
for k, v in ac.__dict__.items():
    print(k, v)
