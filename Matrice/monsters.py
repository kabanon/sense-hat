#!/usr/bin/python3
#-*- coding: utf-8 -*-

class Monter:
  
  def __init__(self, sense, X = (255,255,255), O = (0,0,0)):
    self.monster = None
    self.action  = None
    self.X = X
    self.O = O
    self.position = [0,0]

  def set_X(self, X):
    self.X = X

  def load(self, mid):
    X = self.X
    O = self.O
      
    monsters = {
      '01' : [
        X, O, O, X, X, O, O, X,
        X, O, X, X, X, X, O, X,
        O, X, O, X, X, O, X, O,
        O, X, X, X, X, X, X, O,
        O, X, O, O, O, O, X, O,
        O, O, X, X, X, X, O, O,
        X, X, O, X, X, O, X, X,
        X, O, O, O, O, O, O, X, 
      ],
      '02' : [
        O, X, O, O, O, O, X, O,
        O, X, O, O, O, O, X, O,
        O, O, X, O, O, X, O, O,
        O, O, O, X, X, O, O, O,
        O, O, X, X, X, X, O, O,
        O, X, O, X, X, O, X, O,
        X, X, X, X, X, X, X, X,
        O, X, X, O, O, X, X, O,
      ],
      '03' : [
        O, O, O, X, X, O, O, O,
        O, O, X, X, X, X, O, O,
        O, X, X, X, X, X, X, O,
        X, X, O, X, X, O, X, X,
        X, X, X, X, X, X, X, X,
        O, O, X, X, X, X, O, O,
        O, X, X, X, X, X, X, O,
        X, O, X, O, O, X, O, X,
      ],
    }
    if (mid in monsters):
      self.monster = monsters[mid]

  def display(self):
    # Only return data if monster is defined.
    if (self.monster is not None):
      # Take care of monster position in the matrice.
      _return = list(range(0,64))
      for i in range(0,64,8):
        for j in range(0,8):
          _return[i+j] = self.monster[i+j]
      return _return

  def __str__(self):
    if (self.monster is None):
      return 'No monster loaded'
    else:
      _return = ""
      for i in range(0,64,8):
        for j in range(0,8):
          if (self.monster[i+j] == self.X):
            _return += 'X'
          else:
            _return += ' '
        _return += "\n"
      return _return

       
