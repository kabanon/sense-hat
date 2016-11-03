#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time
from sense_hat import SenseHat
from Matrice import monsters

sense = SenseHat()
sense.clear()
sense.low_light = True

monster = monsters.Monter(sense)
monster.load('01')
sense.set_pixels(monster.monster)
print(monster)
time.sleep(2)
monster.load('02')
sense.set_pixels(monster.monster)
print(monster)
time.sleep(2)
monster.load('03')
sense.set_pixels(monster.monster)
print(monster)
time.sleep(2)

sense.clear()
