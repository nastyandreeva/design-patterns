import math
# Классы с совместимыми интерфейсами: КруглоеОтверстие и
# КруглыйКолышек.
class RoundHole():
    def __init__(self, radius):
        self.radius = radius;

    def getRadius(self):
        return self.radius   # Вернуть радиус отверстия.

    def fits(self, peg):
        return (self.getRadius() >= peg.radius)

class RoundPeg():
    def __init__(self, radius):
        self.radius = radius;

    def getRadius(self):
        return self.radius  # Вернуть радиус круглого колышка.


# Устаревший, несовместимый класс: КвадратныйКолышек.
class SquarePeg():
    def __init__(self, width):
        self.width = width;

    def getWidth(self):
        return self.width   # Вернуть ширину квадратного колышка.


# Адаптер позволяет использовать квадратные колышки и круглые
# отверстия вместе.
class SquarePegAdapter(RoundPeg):
    def __init__(self, peg):
        self.__peg = peg
        self.radius = peg.getWidth() * math.sqrt(2) / 2

    def getRadius(self):
        # Вычислить половину диагонали квадратного колышка по
        # теореме Пифагора.
        return self.radius


# Где-то в клиентском коде.
round_hole = RoundHole(5)
#print(round_hole.radius)
round_peg = RoundPeg(5)
print(round_hole.fits(round_peg)) # TRUE

small_square_peg = SquarePeg(5)
large_square_peg = SquarePeg(10)
#round_hole.fits(small_square_peg) # Ошибка компиляции, AttributeError: 'SquarePeg' object has no attribute 'radius'


small_square_peg_adapter = SquarePegAdapter(small_square_peg)
large_square_peg_adapter = SquarePegAdapter(large_square_peg)
print(round_hole.fits(small_square_peg_adapter)) # TRUE
print(round_hole.fits(large_square_peg_adapter)) # FALSE
