import matplotlib.pyplot as plt

class Shape():

  def __init__(self, base, height, color):
    self.base = base
    self.height = height
    self.color = color
    self.perimeter = 0
    self.area = 0
    self.vertices = []
    self.x_values = []
    self.y_values = []
    self.file_name = ''

  def describe(self):
    print('Base: ' + str(self.base))
    print('Height: ' + str(self.height))
    print('Color: ' + str(self.color))
    print('Perimeter: ' + str(self.perimeter))
    print('Area: ' + str(self.area))
    print('Vertices: ' + str(self.vertices))

  def render(self):
    plt.clf()
    plt.plot(self.x_values,self.y_values, color = self.color, linewidth = 1)
    plt.gca().set_aspect("equal")
    plt.savefig(self.file_name +'.png')


class Rectangle(Shape):

  def __init__(self, base, height, color):
    super().__init__(base, height, color)
    self.perimeter = 2 * base + 2 * height
    self.area = base * height
    self.vertices = [(0,0), (base,0), (base,height), (0,height)]
    self.x_values = [0,base,base,0,0]
    self.y_values = [0,0,height,height,0]
    self.file_name = 'Rectangle'

rect = Rectangle(5,3,'blue')
rect.describe()
rect.render()

class RightTriangle(Shape):

  def __init__(self, base, height, color):
    super().__init__(base, height, color)
    self.perimeter = base + height + (base ** 2 + height ** 2) ** .5
    self.area = base * height / 2
    self.vertices = [(0,0),(base,0), (0,height)]
    self.x_values = [0,0,base,0]
    self.y_values = [0,height,0,0]
    self.file_name = 'RightTriangle'

tri = RightTriangle(4,2,'red')
tri.describe()
tri.render()