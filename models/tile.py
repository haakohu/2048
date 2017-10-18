#/usr/bin/python3

class Tile:
  

  def __init__(self, value=0):
    self.value = value
  
  # Returns active or not
  def is_active(self):
    return self.value != 0
  
  def __str__(self):
    return str(self.value)
  
  def __repr__(self):
    return str(self.value)

  def __eq__(self, other):
    return self.value == other.value