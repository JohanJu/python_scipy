# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:27:17 2015

@author: Admin
"""
from scipy import *
from pylab import *

from Blossoms import Spline
import unittest

class Test(unittest.TestCase):
    def test(self):
        mui= array(range(16))
        dx = array([0,0,0,1,2,3,5,8,10,10,8,6,3,0,0,0])
        dy = array([0,0,0,1,4,6,8,10,10,8,4,2,2,0,0,0])
        s = Spline(mui, dx, dy)
        basisF = s.basisFunction(2, array([0.,1,2,3,4,5,6,7,8,9,10]),3)
        expected = 0.66666666666
        print(basisF(3))
        self.assertAlmostEqual(basisF(3), expected)
        
if __name__ == '__main__':
    unittest.main()
    
#d11 = Alpha(u,ui[I+1],ui[I-2])*d[I-2]+(1-Alpha(u,ui[I+1], ui[I-2]))*d[I-1]
#d12 = Alpha(u, ui[I+2], ui[I-1])*d[I-1]+(1-Alpha(u,ui[I+2], ui[I-1]))*d[I]
#d13 = Alpha(u, ui[I+3], ui[I])*d[I]+(1-Alpha(u,ui[I+3], ui[I]))*d[I+1]
#    
#d21 = Alpha(u, ui[I+1], ui[I-1])*d11+(1-Alpha(u,ui[I+1], ui[I-1]))*d12
#d22 = Alpha(u, ui[I+2], ui[I])*d12+(1-Alpha(u,ui[I+2], ui[I]))*d13
#    
#return Alpha(u, ui[I+1], ui[I])*d21+(1-Alpha(u,ui[I+1], ui[I]))*d22 