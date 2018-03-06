class Rectangle:
  def __init__(self, length, width):
    
    self.length = length
    self.width = width
    self.validateDimension()
    
  
  def validateDimension(self):
  
    try:
      self.width = float(self.width)
      self.length = float(self.length)
    except ValueError:
      raise ValueError("Dimensions can not be converted to integer")
  
  
     
  def area(self):
    return self.length * self.width
  
  def perimeter(self):
    return 2*(self.length + self.width)
 
invalid = Rectangle("6","5")
print(invalid.area())