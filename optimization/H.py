# -*- coding: utf-8 -*-
from Generic import QuasiNewton
from scipy import *
import sys
class BadBroyden(QuasiNewton):
    def __call__(self,H,delta,gamma):
        return h #some update
        
class GoodBroyden(QuasiNewton):
    def nextH(self,H,delta,gamma):
        print("H",H)
        print("delta",delta)
        print("gamma",gamma)
        sys.stdout.flush()
        u = delta-H.dot(gamma);
        print("u",u)
        uTranspose = u.transpose()
        print("t",(u.dot(uTranspose)))
        print("n",(uTranspose.dot(gamma)))
        print("re ",H+(u.dot(uTranspose))/(uTranspose.dot(gamma)))
        sys.stdout.flush()
        return H+(u.dot(uTranspose))/(uTranspose.dot(gamma))

class DFPRank2Update(QuasiNewton):    
    def nextH(self,H,delta,gamma):
        deltaTranspose = delta.transpose()
        gammaTranspose = gamma.transpose()
        HTimesGamma = H.dot(gamma)
        term1 = (delta.dot(deltaTranspose))/(deltaTranspose.dot(gamma))
        term2 = (HTimesGamma.dot(gammaTranspose.dot(H)))/(gammaTranspose.dot(HTimesGamma))  
        return H + term1 - term2

class BFGSRank2Update(QuasiNewton):  
    def call(self,H,delta,gamma):
        deltaTranspose = delta.transpose()
        gammaTranspose = gamma.transpose()
        gammaTransposeTimesH = gammaTranspose*H
        deltaTransposeTimesGamma= deltaTranspose*gamma
        factor1 = 1 + (gammaTransposeTimesH*gamma)/deltaTransposeTimesGamma
        factor2 = (delta*deltaTranspose)/deltaTransposeTimesGamma
        term = (delta*gammaTransposeTimesH+H*gamma*deltaTranspose)/deltaTransposeTimesGamma
        return H + factor1*factor2 - term