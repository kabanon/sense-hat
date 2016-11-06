#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time
from Matrice import monsters

def demo(mid = '01'):
  monster = monsters.Monter()
  monster.load(mid)
  monster.position['x'] = 8
  if (mid == '02'):
    monster.colors[0] = (10,10,10)
    monster.colors[1] = (255,0,0)
  for i in range(0, 15):
    monster.move_left()
  for i in range(0, 15):
    monster.move_right()
  for i in range(0, 8):
    monster.move_left()
  for i in range(0, 8):
    monster.move_top()
  for i in range(0, 15):
    monster.move_bottom()
  if (mid == '01'):
    demo('02')


if __name__ == '__main__':
  demo()
  
