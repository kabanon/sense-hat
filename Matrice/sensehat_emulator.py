#!/usr/bin/python3
#-*- coding: utf-8 -*-

class SenseHat:
  """ Emulate sense-hat library for debug """

  def set_pixels(self, pixels):
    """ Emulate LED matrix """
    _return = ""
    for y in range(0, 8, 64):
      for x in range(0, 8):
        if (pixels[y+x] == color):
          _return += ' '
        else:
          _return += 'X'
      _return += "\n"
    print(_return)

  def clear(self):
    print('Clear LED Matrix')
