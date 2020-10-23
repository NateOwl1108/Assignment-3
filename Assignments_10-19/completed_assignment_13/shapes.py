import matplotlib.pyplot as plt

class Rectangle():

  def __init__(self, base, height, color):
    self.base = base
    self.height = height
    self.color = color
    self.perimeter = 2 * base + 2 * height
    self.area = base * height
    self.vertices = [(0,0),(base,0),(base,height), (0,height)]
  
  def describe(self):
    print('Base: ' + str(self.base))
    print('Height: ' + str(self.height))
    print('Color: ' + str(self.color))
    print('Perimeter: ' + str(self.perimeter))
    print('Area: ' + str(self.area))
    print('Vertices: ' + str(self.vertices))

  def render(self):
    x_values = [0,self.base,self.base,0,0]
    y_values = [0,0,self.height,self.height,0]
    plt.plot(x_values,y_values, color = self.color, linewidth = 1)
    plt.gca().set_aspect("equal")
    plt.savefig('Rectangle.png')

class Square(Rectangle):
  def __init__(self, side, color):
    super().__init__(side, side, color)

sq = Square(5,'green')
sq.describe()
sq.render()
