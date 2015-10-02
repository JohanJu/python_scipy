# -*- coding: utf-8 -*-

from H import BadBroyden
from Line import ExactLine
from Generic import QuasiNewton
from Problem import Problem

def f(x):
    return [i ** 2 for i in x]

qn = QuasiNewton(Problem(f),BadBroyden(),ExactLine())
print(qn.slove(array([1,1]),0.01))

    




