class Point:

    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y
point = make_object(Point, 5, 10)
point2 = copy.deepcopy(point)
