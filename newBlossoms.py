# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:22:56 2015

@author: Admin
"""
ui= array(range(16))
d = array([0,0,0,1,4,6,8,0,10,8,4,2,2,0,0,0])

def Alpha(u, rm, lm):
    return (rm-u)/(rm-lm)

def Blossom(u, I):
    d11 = Alpha(u,ui[I+1],ui[I-2])*d[I-2]+(1-Alpha(u,ui[I+1], ui[I-2]))*d[I-1]
    d12 = Alpha(u, ui[I+2], ui[I-1])*d[I-1]+(1-Alpha(u,ui[I+2], ui[I-1]))*d[I]
    d13 = Alpha(u, ui[I+3], ui[I])*d[I]+(1-Alpha(u,ui[I+3], ui[I]))*d[I+1]
    
    d21 = Alpha(u, ui[I+2], ui[I-2])*d11+(1-Alpha(u,ui[I+2], ui[I-2]))*d12
    d22 = Alpha(u, ui[I+3], ui[I-1])*d12+(1-Alpha(u,ui[I+3], ui[I-1]))*d13
    
    return Alpha(u, ui[I+3], ui[I-2])*d21+(1-Alpha(u,ui[I+3], ui[I-2]))*d22   

y=[]
for i in range(2,12):
    y.append(Blossom(i, i))

plot(range(2,12),y)



