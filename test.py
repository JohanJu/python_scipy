# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:27:17 2015

@author: Admin
"""
from scipy import *
from pylab import *

from Blossoms import Spline
from Blossoms import BlossomSpline
import unittest

class Test(unittest.TestCase):
    def test(self):
        ui= array(range(16))
        d = array([0,0,0,1,4,6,8,10,10,8,4,2,2,0,0,0])
        s = Spline(ui, d)
        bs = BlossomSpline(ui,d)
        l = linspace(3,11,20)
        for i in l:
           self.assertAlmostEqual(bs(i), s(i))
           print("point ",i," tested")
        
        
if __name__ == '__main__':
    unittest.main()