# -*- coding: utf-8 -*-
# @author: Caroline Brandberg, Johan Ju
from Generic import QuasiNewton
from scipy import *
import sys
class BadBroyden(QuasiNewton):
    def nextH(self,H,delta,gamma):
        u = (delta-H*gamma)/(gamma.transpose()*gamma)
        return H+(u*gamma.transpose())
        
class GoodBroyden(QuasiNewton):
    def nextH(self,H,delta,gamma):
        u = delta-H*gamma;
        uT = u.transpose()
        return H+(u*uT)/(uT*gamma)

class DFPRank2Update(QuasiNewton):
    def nextH(self,H,delta,gamma):
        dT = delta.transpose()
        gT = gamma.transpose()
        H_dot_g = H*gamma
        term1 = (delta*dT)/(dT*gamma)
        term2 = (H_dot_g*gT*H)/(gT*H_dot_g)
        return H + term1 - term2

class BFGSRank2Update(QuasiNewton):
    def nextH(self,H,delta,gamma):
        dT = delta.transpose()
        gT = gamma.transpose()
        gT_dot_H = gT*H
        dT_dot_g= dT*gamma
        factor1 = eye(len(delta)) + (gT_dot_H*gamma)/dT_dot_g
        factor2 = (delta*dT)/dT_dot_g
        term = (delta*gT_dot_H+H*gamma*dT)/dT_dot_g
        return H + factor1*factor2 - term