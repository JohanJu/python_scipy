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
        mui= array(range(16))
        dx = array([0,0,0,1,2,3,5,8,10,10,8,6,3,0,0,0])
        dy = array([0,0,0,1,4,6,8,10,10,8,4,2,2,0,0,0])
        s = Spline(mui, dx, dy)
        bs = BlossomSpline(mui,dx,dy)
        l = linspace(3,11,20)
        for i in l:
           self.assertAlmostEqual(bs(i), s(i))
           print("point ",i," tested")
        
        
if __name__ == '__main__':
    unittest.main()