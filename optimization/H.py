# -*- coding: utf-8 -*-
from scipy import *
class BadBroyden():
    def __call__(self,h,delta,gamma):
        return h #some update
        
class GoodBroyden():
    def __call__(self,h,delta,gamma):
        return h #some update

class DFPRank2Update():    
    def __call__(self,H,delta,gamma):
        deltaTranspose = delta.transpose()
        gammaTranspose = gamma.transpose()
        HTimesGamma = H*gamma
        term1 = (delta*deltaTranspose)/(deltaTranspose*gamma)
        term2 = (HTimesGamma*gammaTranspose*H)/(gammaTranspose*HTimesGamma)
        return H + term1 - term2

class BFGSRank2Update():  
    def call(self,H,delta,gamma):
        deltaTranspose = delta.transpose()
        gammaTranspose = gamma.transpose()
        gammaTransposeTimesH = gammaTranspose*H
        deltaTransposeTimesGamma= deltaTranspose*gamma
        factor1 = 1 + (gammaTransposeTimesH*gamma)/deltaTransposeTimesGamma
        factor2 = (delta*deltaTranspose)/deltaTransposeTimesGamma
        term = (delta*gammaTransposeTimesH+H*gamma*deltaTranspose)/deltaTransposeTimesGamma
        return H + factor1*factor2 - term