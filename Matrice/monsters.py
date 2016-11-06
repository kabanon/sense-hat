#!/usr/bin/python3
#-*- coding: utf-8 -*-

import json
import os

from . import matrix

class Monter(matrix.Matrix):

  def load(self, mid):
    """ Load monster from json file """
    filename = "{}/json_monsters/{}.json".format(os.path.dirname(os.path.abspath(__file__)), mid)
    try:
      with open(filename) as json_data:
        self.matrix = json.load(json_data)
        json_data.close()
    except IOError: 
        print("Error: File '{}' does not appear to exist.".format(filename))

       
