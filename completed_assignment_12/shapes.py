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

rect = Rectangle(5,2,'red')
rect.describe()
rect.render()

class RightTriangle():

  def __init__(self, base, height, color):
    self.base = base
    self.height = height
    self.color = color
    self.perimeter = base + height + (base ** 2 + height ** 2) ** .5
    self.area = base * height / 2
    self.vertices = [(0,0),(base,0), (0,height)]
  
  def describe(self):
    print('Base: ' + str(self.base))
    print('Height: ' + str(self.height))
    print('Color: ' + str(self.color))
    print('Perimeter: ' + str(self.perimeter))
    print('Area: ' + str(self.area))
    print('Vertices: ' + str(self.vertices))

  def render(self):
    x_values = [0,0,self.base,0]
    y_values = [0,self.height,0,0]
    plt.clf()
    plt.plot(x_values,y_values, color = self.color, linewidth = 1)
    plt.gca().set_aspect("equal")
    plt.savefig('Triangle.png')

tri = RightTriangle(5,2,'blue')
tri.describe()
tri.render()
