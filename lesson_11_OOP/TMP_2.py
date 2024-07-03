class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return 'Rectangle [a = ' + str(self.a) + ', b = ' + str(self.b) + ']'


reсtangle_1 = Rectangle(4, 5)

print(reсtangle_1.get_area())
print(reсtangle_1)
