# -*- coding: utf-8 -*-
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
        deltaTranspose = delta.transpose()
        gammaTranspose = gamma.transpose()
        HTimesGamma = H.dot(gamma)
        term1 = (delta.dot(deltaTranspose))/(deltaTranspose.dot(gamma))
        term2 = (HTimesGamma.dot(gammaTranspose.dot(H)))/(gammaTranspose.dot(HTimesGamma))  
        return H + term1 - term2

class BFGSRank2Update(QuasiNewton):  
    def nextH(self,H,delta,gamma):
        deltaTranspose = delta.transpose()
        gammaTranspose = gamma.transpose()
        gammaTransposeTimesH = gammaTranspose*H
        deltaTransposeTimesGamma= deltaTranspose*gamma
        factor1 = eye(len(delta)) + (gammaTransposeTimesH*gamma)/deltaTransposeTimesGamma
        factor2 = (delta*deltaTranspose)/deltaTransposeTimesGamma
        term = (delta*gammaTransposeTimesH+H*gamma*deltaTranspose)/deltaTransposeTimesGamma
        return H + factor1*factor2 - term