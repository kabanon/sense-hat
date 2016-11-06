#!/usr/bin/python3
#-*- coding: utf-8 -*-

import json
import os

class Monter():
  
  def __init__(self):
    self.monster = None
    self.colors = {
      0 : (0,0,0),
      1 : (255,255,255)
    }
    self.position = {
      'x':0,
      'y':0,
    }
    self.step = 8
    self.size = self.step * self.step


  def set_X(self, X):
    self.X = X

  def load(self, mid):      
    filename = "{}/json_monsters/{}.json".format(os.path.dirname(os.path.abspath(__file__)), mid)
    try:
      with open(filename) as json_data:
        self.monster = json.load(json_data)
        json_data.close()
    except IOError: 
        print("Error: File '{}' does not appear to exist.".format(filename))

  def display(self):
    _return = list(range(0, self.size))
    # Only return data if monster is defined.
    if (self.monster is not None):
      for y in range(0, self.size, self.step):
        for x in range(0, self.step):
          _pos = y+x
          # Define a default value. 
          _return[_pos] = self.colors[0]
          # Check if x position is in visible area
          _check_x = x - self.position['x']
          if (_check_x >= 0 and _check_x < self.step):
            # Check if y position is in visible area
            _check_y = int(y / self.step - self.position['y']) * self.step
            if (_check_y >= 0 and _check_y < self.size):
              # Get pixel to display 
              _return[_pos] = self.colors.get(self.monster[_check_x+_check_y], self.colors[0])
    return _return

  def __str__(self):
    if (self.monster is None):
      return 'No monster loaded'
    else:
      _return = ""
      for i in range(0,64,8):
        for j in range(0,8):
          if (self.monster[i+j] >= 1):
            _return += 'X'
          else:
            _return += ' '
        _return += "\n"
      return _return

       
