#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time
from Matrice import monsters

monster = monsters.Monter()

monster.load('01')

for i in range(0, 7):
  monster.move_left()
