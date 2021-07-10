class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def get_full_profit(self, weight=25, thickness=5):
        return f"{self._length} m * {self._width} m * {weight} kg * {thickness} cm =" \
               f"{(self._length * self._width * weight * thickness) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())
