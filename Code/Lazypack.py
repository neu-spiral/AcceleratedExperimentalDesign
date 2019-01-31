#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 00:17:05 2018

@author: yuanneu
"""

import time
import heapq as hq
import numpy as np
from Greedypack import *

class LazyGreedy(Greedy):
    """ A generic abstract class implementing the simple greedy algorithm."""

    def __init__(self,f,Omega):
        """Initialize by providing submodular function as well as universe Omega over which elements are selected. 
        """
        self.f=f
        self.Omega=Omega

    def initializeS(self):
        """Initialize set S.
        """
        Greedy.initializeS(self)
        self.heap=[(self.f([e]),e) for e in self.Omega]
        hq.heapify(self.heap)
    
    def greedyGrow(self,k):
        """Construct greedy set.
        """
        Time=[]
        t1=time.time()
        while (True):
            e=hq.heappop(self.heap)[1]            
            self.updateS(e)
            t2=time.time()
            Time.append(t2-t1)
            if len(self.S)>=k:
                break
            t1=time.time()
            value,e=self.heap[0]
            done=None
            while not done:
                item_renew=self.MarginalGain(e),e
                hq.heapreplace(self.heap, item_renew)
                value,opti=self.heap[0]
                if opti==e:
                    done=True
                else:
                    e=opti            
        return self.getScopy(),Time   #self.f(self.S))
    
    def MarginalGain(self,e):
        """Marginal Gain for a key e
        """
        val1=self.evalSAddX(e)
        val2=self.f(self.S)
        value=val1-val2
        return value
             
class NaiveLazy(LazyGreedy):
    def __init__(self,Xarray,Omega,InvA):
        """Initialize by providing submodular function as well as universe Omega over which elements are selected. 
        """
        self.Xarray=Xarray
        self.n,self.d=np.shape(self.Xarray)
        self.InvA=InvA
        self.Omega=Omega
    
    def initializeS(self):
        """Initialize set S and build up a heap.
        """ 
        Greedy.initializeS(self)
        Ut=np.linalg.cholesky(self.InvA)
        self.Zsave=np.dot(self.Xarray,Ut)
        def mapf(e):
            zdiff=self.Zsave[e[0],:]-self.Zsave[e[1],:]
            return -np.dot(zdiff,zdiff)                   
        self.heap=[(mapf(e),e) for e in self.Omega]
        hq.heapify(self.heap)
    
    def updateS(self,e):
        """ adapt the new key to the set S
        """
        LazyGreedy.updateS(self,e)
        self.InvA=shermanMorissonUpdate(self.InvA,self.Xarray[e[0],:]-self.Xarray[e[1],:])
            
    def MarginalGain(self,e):
        x_ij=self.Xarray[e[0],:]-self.Xarray[e[1],:]
        return -np.dot(x_ij,np.dot(self.InvA,x_ij))
                    
class FactorizationLazy(NaiveLazy):                
    def updateS(self,e):
        NaiveLazy.updateS(self,e)
        Ut=np.linalg.cholesky(self.InvA)
        self.Zsave=np.dot(self.Xarray,Ut)
        
    def MarginalGain(self,e):
        z_ij=self.Zsave[e[0],:]-self.Zsave[e[1],:]
        return -np.dot(z_ij,z_ij)
        
class DeMem(dict): 
    """ Memoization class for Decomposition Lazygreedy
    """
    def __init__(self,g):
        self.g=g
    def get(self,key): 
        #if key in self:
        try:
            return self[key]                        
        except:
            self[key]=self.g(key)
            return self[key]
                
class FactorizationLazyMemo(NaiveLazy):                
    def updateS(self,e):
        NaiveLazy.updateS(self,e)
        Ut=np.linalg.cholesky(self.InvA)
        def fun(key, Xarray, U):
            y=np.dot(Xarray[key,:],U)
            return y
        f1=lambda key: fun(key, self.Xarray, Ut)
        self.Zsave=DeMem(f1)
        
    def MarginalGain(self,e):
        z_ij=self.Zsave.get(e[0])-self.Zsave.get(e[1])
        return -np.dot(z_ij,z_ij)
    

class ScalarLazy(NaiveLazy):
    def initializeS(self):
        """Initialize set S.
        """ 
        Greedy.initializeS(self)
        Ut=np.linalg.cholesky(self.InvA)
        self.Zsave=np.dot(self.Xarray,Ut)
        def mapf(e):
            zdiff=self.Zsave[e[0],:]-self.Zsave[e[1],:]
            return -np.dot(zdiff,zdiff)                   
        self.heap=[(mapf(e),e,0) for e in self.Omega]
        hq.heapify(self.heap)
        self.degree=0
        self.Scalar=np.zeros((400,self.n))
        
    def updateS(self,e):
        
        xdiff=self.Xarray[e[0],:]-self.Xarray[e[1],:]
        V=np.dot(self.InvA,xdiff)*np.sqrt(1/(1+np.dot(xdiff,np.dot(self.InvA,xdiff))))
        Vx=np.dot(self.Xarray,V)
        self.Scalar[self.degree,:]=Vx
        self.degree+=1
        NaiveLazy.updateS(self,e) 
        
    def greedyGrow(self,k):
        """Construct greedy set.
        """
        Time=[]
        t1=time.time()
        while (True):
            e=hq.heappop(self.heap)[1]
            self.updateS(e)
            t2=time.time()
            Time.append(t2-t1)
            if len(self.S)>=k:
                break
            t1=time.time()
            value,e,degree=self.heap[0]
            done=None
            while not done:
                item_renew=self.ItemAdapt(value,e,degree)
                hq.heapreplace(self.heap, item_renew)
                value,opti,degree=self.heap[0]
                if opti==e:
                    done=True
                else:
                    e=opti
        return self.getScopy(),Time   #self.f(self.S)) 
    
    def ItemAdapt(self,value,e,degree):
        (key1,key2)=e
        z_sumlist=range(degree,self.degree) 
        gap_v=self.Scalar[z_sumlist,key1]-self.Scalar[z_sumlist,key2]
        value+=np.dot(gap_v,gap_v) 
        return (value,e,self.degree)
 
class ScalarLazyMemo(ScalarLazy):
    def initializeS(self):
        """Initialize set S.
        """ 
        ScalarLazy.initializeS(self)
        self.V={}
        def f(x):
            pass
        self.Rho=DeMem(f)
                
    def updateS(self,e):
        xdiff=self.Xarray[e[0],:]-self.Xarray[e[1],:]
        self.V[self.degree]=np.dot(self.InvA,xdiff)*np.sqrt(1/(1+np.dot(xdiff,np.dot(self.InvA,xdiff))))
        def fun(key, Xarray, Vdict):
            y=np.dot(Xarray[key[1],:], Vdict[key[0]])
            return y
        f=lambda key: fun(key, self.Xarray, self.V)    
        self.Rho.g=f
        self.degree+=1
        NaiveLazy.updateS(self,e)  
        
    def ItemAdapt(self,value,e,degree):
        (key1,key2)=e
        for pac in range(degree,self.degree):
            value+=(self.Rho.get((pac,key1))-self.Rho.get((pac,key2)))**2
        return (value,e,self.degree)
