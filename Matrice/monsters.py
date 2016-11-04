#!/usr/bin/python3
#-*- coding: utf-8 -*-

import json
import os

class Monter:
  
  def __init__(self):
    self.monster = None
    self.action  = None
    self.colors = {
      0 : (0,0,0),
      1 : (255,255,255)
    }
    self.position = [0,0]

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
    # Only return data if monster is defined.
    if (self.monster is not None):
      # Take care of monster position in the matrice.
      _return = list(range(0,64))
      for i in range(0,64,8):
        for j in range(0,8):
          _return[i+j] = self.colors.get(self.monster[i+j], (0,0,0))
      return _return

  def __str__(self):
    if (self.monster is None):
      return 'No monster loaded'
    else:
      _return = ""
      for i in range(0,64,8):
        for j in range(0,8):
          if (self.monster[i+j] == 1):
            _return += 'X'
          else:
            _return += ' '
        _return += "\n"
      return _return

       
