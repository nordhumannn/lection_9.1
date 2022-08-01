class Box:

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def sum_volume(box_1, box_2):
        return box_1.volume() + box_2.volume()

    def __str__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z}'


box_1 = Box(2, 3, 4)
box_2 = Box(3, 4, 5)

print(box_1.sum_volume(box_2))
print(Box.sum_volume(box_1, box_2))
