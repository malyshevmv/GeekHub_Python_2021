"""
3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням
white і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square)
містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.
"""


class Figure(object):
    color = 'white'

    def change_the_color_of_the_figure(self, color_figure):
        self.color = color_figure


class Oval(Figure):
    def __init__(self, circuit):
        self.circuit = circuit


class Square(Figure):
    def __init__(self, length_square):
        self.length_square = length_square


ab = Square(2)
ab.change_the_color_of_the_figure('black')
print(ab.color)