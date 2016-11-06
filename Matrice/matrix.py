#!/usr/bin/python3
#-*- coding: utf-8 -*-

class Matrix():
  
  def __init__(self):
    """ Initialize the matrix """
    self.matrix = None
    self.colors = {
      0 : (0,0,0),
      1 : (255,255,255)
    }
    self.position = {
      'x':0,
      'y':0,
    }
    self.size = {
      'x' : 8,
      'y' : 8,
    }
    self.size['range'] = self.size['x'] * self.size['y']

  def move(self, x = 0, y = 0):
    """ Move the matrix on sense-hat display. """
    self.position['x'] += x
    self.position['y'] += y

  def move_left(self, x=1):
    """ Move the matrix to the left """
    self.move(x = -x)

  def move_right(self, x=1):
    """ Move the matrix to the right """
    self.move(x = x)

  def move_top(self, y=1):
    """ Move the matrix up """
    self.move(y = -y)

  def move_bottom(self, y=1):
    """ Move the matrix below """ 
    self.move(y = y)

  def display(self):
    """ Display the matrix on sense-hat LED matrix """
    # Only return data if the matrix is defined.
    if (self.matrix is not None):
      _return = list(range(0, self.size['range']))
      for y in range(0, self.size['range'], self.size['y']):
        for x in range(0, self.size['x']):
          _pos = y+x
          # Define a default value. 
          _return[_pos] = self.colors[0]
          # Check if x position is in visible area
          _check_x = x - self.position['x']
          if (_check_x >= 0 and _check_x < self.size['x']):
            # Check if y position is in visible area
            _check_y = int(y / self.size['y'] - self.position['y']) * self.size['y']
            if (_check_y >= 0 and _check_y < self.size['range']):
              # Get pixel to display 
              _return[_pos] = self.colors.get(self.matrix[_check_x+_check_y], self.colors[0])
      return _return

  def __str__(self):
    """ Print the matrix with this magic method """
    if (self.matrix is None):
      return 'No matrix loaded'
    else:
      _matrix = self.display()
      _return = ""
      for i in range(0,64,8):
        for j in range(0,8):
          if (_matrix[i+j] == self.colors[0]):
            _return += ' '
          else:
            _return += 'X'
        _return += "\n"
      return _return

       
