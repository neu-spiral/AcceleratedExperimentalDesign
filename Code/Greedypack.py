#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 00:34:37 2018

@author: yuanneu
"""

import numpy as np
import math
import time
from mathpackage import *


class Greedy():
    """ A generic abstract class implementing the simple greedy algorithm."""

    def __init__(self,f,Omega):
        """Initialize by providing submodular function as well as universe Omega over which elements are selected. 
        """
        self.f=f
        self.Omega=Omega


    def initializeS(self):
        """Initialize set S.
        """
        #self.S = set()
        self.S=[]
        self.Remainder = self.Omega.copy()

    def updateS(self,x):
        """Update current set S with element x.
        """
        #self.S.add(x)
        self.S.append(x)
        self.Remainder.remove(x)
        
    def eval(self,S=None):
        if S==None:
            return self.f(self.S)
        else:
            return self.f(S)

    def getScopy(self):
        return self.S

    def getRemainderCopy(self):
        return self.Remainder.copy()
   
    def evalSAddX(self,i):
        self.S.append(i)
        val=self.f(self.S)
        self.S.remove(i)
        return val
        

    def greedyGrow(self,k):
        """Construct greedy set.
        """
        Time=[]
        time1=time.time()
        while len(self.S)<k:
            maxVal = float("-inf")
            for i in self.Remainder:
               val = self.evalSaddX(i)
               if val>maxVal:
                   maxVal=val
                   opti = i 
            self.updateS(opti) 
            time2=time.time()
            Time.append(time2-time1)
            time1=time.time()
        return self.getScopy(),Time   #self.f(self.S))

class NaiveGreedy(Greedy):
    """Naive Greedy Algorithm"""

    def __init__(self,Xarray,Omega,InvA0=None):
        """Initialization"""
        self.Xarray = Xarray
        self.n,self.d= np.shape(Xarray)
        self.Omega = Omega
        try:
            self.InvA0=InvA0
        except:
            self.InvA0=np.eye(d)
        

    def initializeS(self):
        """Initialize set S.
        """
        Greedy.initializeS(self)
        self.InvA = self.InvA0.copy()


    def updateS(self,pair):
        Greedy.updateS(self,pair)
        self.x = self.Xarray[pair[0],:]-self.Xarray[pair[1],:]
        self.InvA =shermanMorissonUpdate(self.InvA,self.x)
       
    def evalSaddX(self,pair):
        x = self.Xarray[pair[0],:]-self.Xarray[pair[1],:]
        z = np.dot(self.InvA,x)
        return np.dot(x,z)
  
    
class DecompositionGreedy(NaiveGreedy): 
    def initializeS(self):
        NaiveGreedy.initializeS(self)
        Ut=np.linalg.cholesky(self.InvA)
        self.Zsave=np.dot(self.Xarray,Ut)


    def updateS(self,pair):
        NaiveGreedy.updateS(self,pair)
        Ut=np.linalg.cholesky(self.InvA)
        self.Zsave=np.dot(self.Xarray,Ut)
       
 
    def evalSaddX(self,pair):
        d_ij=self.Zsave[pair[0],:]-self.Zsave[pair[1],:]
        return np.dot(d_ij,d_ij)
   
    	 
class MemoizationGreedy(DecompositionGreedy):
    def initializeS(self):
        DecompositionGreedy.initializeS(self)
        Nsize=np.shape(self.Xarray)[0]
        self.Zdict={}
        for pi in range(Nsize):
            for pj in range(pi+1,Nsize):
                z_ij=self.Zsave[pi,:]-self.Zsave[pj,:]
                self.Zdict[(pi,pj)]=np.dot(z_ij,z_ij)

        del self.Zsave #uncomment if you want to save memory


    def evalSaddX(self,pair):
        return self.Zdict[pair] 


    def updateS(self,pair):
        invAprev = self.InvA
        NaiveGreedy.updateS(self,pair)
        vr=np.dot(invAprev,self.x)*np.sqrt(1/(1+np.dot(self.x,np.dot(invAprev,self.x))))

        Zvector=np.dot(self.Xarray,vr)
        Nsize=np.shape(self.Xarray)[0]
        for pi in range(Nsize):
            for pj in range(pi+1,Nsize):
                self.Zdict[(pi,pj)]=self.Zdict[(pi,pj)]-(Zvector[pi]-Zvector[pj])**2


