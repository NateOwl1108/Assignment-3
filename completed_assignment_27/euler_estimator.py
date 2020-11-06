import matplotlib.pyplot as plt
plt.style.use('bmh')

class EulerEstimator():
  def __init__(self, derivative, point):
    self.derivative = derivative
  
  def calc_derivative_at_point(self, point):
    
    x_value = point[0]
    y_value = point[1]
    return self.derivative(x_value)

  def step_forward(self,point, step):
    x_value = point[0]
    y_value = point[1]
    y_value += step * self.calc_derivative_at_point(point)
    y_value = round(y_value, 2)
    x_value += step
    x_value = round(x_value, 2)
    
    return [x_value, y_value]
  
  def calc_estimated_points(self, initial_point , step_size, num_steps):
    x_value = point[0]
    y_value = point[1]
    for i in range(num_steps):
      self.step_forward(step_size)
      print(self.step_forward(step_size))

  def plot(self, point , step_size, num_steps):
    x_value = point[0]
    y_value = point[1]
    x_values = [x_value]
    y_values = [y_value]
    for i in range(num_steps):
      values = self.step_forward(point, step_size)
      
      x_values.append(values[0])
      y_values.append(values[1])
      point = (values[0],values[1])
    plt.plot(x_values,y_values,linewidth = 0.75 )
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('EulerEstimator')
    plt.savefig('EulerEstimator.png')




euler = EulerEstimator(derivative = (lambda t: t+1),
                           point = (1,4))

euler.plot(point=[-5,10], step_size=0.1, num_steps=100)