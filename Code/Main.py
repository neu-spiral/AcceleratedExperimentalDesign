#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 22:11:22 2018

@author: yuanneu
"""
import pickle
from experimental4 import *
import sys
from Greedypack import *
from Lazypack import *

 
def AppendY(Xm,Ym):
    n,d=np.shape(Xm)
    Xa=np.concatenate((Xm,np.zeros((1,d))),0)
    if Ym[0]==1:
        Ya=np.concatenate((Ym,np.array([-1])))
    else:
        Ya=np.concatenate((Ym,np.array([1])))
    return Xa,Ya 

def TimeTransfer(timetotal,Timelist):
    Time=[]
    for i in range(len(Timelist)):
        Time.append(timetotal)
        timetotal-=Timelist[-i-1]
    TimeR=Time.reverse()
    Ta=np.array(Time)
    return Ta


def AUCReturn(Xab,Yab,Xarray,Ycom,Xlist,Ylist,listt,Clist):  
    [Xtest1,Xtest2,Xtest3,Xtest4]=Xlist
    [Ytest1,Ytest2,Ytest3,Ytest4]=Ylist
    X1=Xab.copy()
    Y1=Yab.copy()
    X1,Y1=AppendY(X1,Y1)
    Aclist=[]       
    for (ki,kj) in listt:
        Auclist1=[]
        Auclist2=[]
        Auclist3=[]
        Auclist4=[]
        Xfeature=np.array([Xarray[ki,:]-Xarray[kj,:]])
        Ylabel=np.array([Ycom[(ki,kj)]])
        X1=np.concatenate((X1,Xfeature),0)
        Y1=np.concatenate((Y1,Ylabel))
        for C_value in Clist:
            clf=LogisticRegression(C=C_value,fit_intercept=True, penalty='l2', tol=0.01)             
            clf.fit(X1,Y1)
            b1=clf.coef_[0] 
            score1=np.dot(Xtest1,b1) 
            score2=np.dot(Xtest2,b1)
            score3=np.dot(Xtest3,b1)
            score4=np.dot(Xtest4,b1)
                
            auc1=roc_auc_score(Ytest1,score1)
            auc2=roc_auc_score(Ytest2,score2)
            auc3=roc_auc_score(Ytest3,score3)
            auc4=roc_auc_score(Ytest4,score4)
            Auclist1.append(auc1)
            Auclist2.append(auc2)
            Auclist3.append(auc3)
            Auclist4.append(auc4)
        Alist=[Auclist1,Auclist2,Auclist3,Auclist4]
        Aa=np.array(Alist)
        Aclist.append(Aa)
    return np.array(Aclist)

timefa1=float(sys.argv[1])
ddt=int(timefa1)
covs=float(sys.argv[2])
hyper=1*covs
fold=float(sys.argv[3])
ft=int(fold)


Name = 'Ndata'
Size1=200
Size2=8
Size3=10
for fold in range(ft,ft+1):
    cst=Name+str(ddt)+'ddt'+str(fold)+'.p'
    file=open(cst,'rb')
    Cp=pickle.load(file)
    
    Xarray=Cp['Xarray']
    Yab=Cp['Yab']
    Xab=Cp['Xab']
    Omega=Cp['Omega']
    Ycom=Cp['Ycom']
    Xtest=Cp['Xtest']
    Ytest=Cp['Ytest']
    Xval=Cp['Xval']
    Yval=Cp['Yval']
    Xctest=Cp['Xctest']
    Yctest=Cp['Yctest']
    Xcval=Cp['Xcval']
    Ycval=Cp['Ycval']
    
    invA1=1/hyper*np.eye(np.shape(Xab)[1])
    for i in range(np.shape(Xab)[0]):
        invA1=shermanMorissonUpdate(invA1,Xab[i,:])  
    t1=time.time()
    b1=NaiveGreedy(Xarray,Omega,invA1)
    b1.initializeS()
    c1,T1=b1.greedyGrow(Size1) 
    t2=time.time()
    Ta1=TimeTransfer(t2-t1,T1)

    t2=time.time()
    b2=DecompositionGreedy(Xarray,Omega,invA1)
    b2.initializeS()
    c2,T2=b2.greedyGrow(Size1) 
    t3=time.time()
    Ta2=TimeTransfer(t3-t2,T2)
    
    t3=time.time() 
    b3=MemoizationGreedy(Xarray,Omega,invA1)
    b3.initializeS()
    c3,T3=b3.greedyGrow(Size1) 
    t4=time.time()
    Ta3=TimeTransfer(t4-t3,T3)
    
    t4=time.time()
    b4=NaiveLazy(Xarray,Omega,invA1)
    b4.initializeS()
    c4,T4=b4.greedyGrow(Size1)
    t5=time.time()
    Ta4=TimeTransfer(t5-t4,T4)
    
    t5=time.time()
    b5=DecompositionLazy(Xarray,Omega,invA1)
    b5.initializeS()
    c5,T5=b5.greedyGrow(Size1)    
    t6=time.time()
    Ta5=TimeTransfer(t6-t5,T5)
    
    t6=time.time()
    b6=DecomLazyMemo(Xarray,Omega,invA1)
    b6.initializeS()
    c6,T6=b6.greedyGrow(Size1)
    t7=time.time()
    Ta6=TimeTransfer(t7-t6,T6)
    
    t7=time.time()
    b7=ScalarLazy(Xarray,Omega,invA1)  
    b7.initializeS()
    c7,T7=b7.greedyGrow(Size1) 
    t8=time.time()
    Ta7=TimeTransfer(t8-t7,T7)
    
    t8=time.time()
    b8=ScalarLazyMemo(Xarray,Omega,invA1)
    b8.initializeS()
    c8,T8=b8.greedyGrow(Size1)
    t9=time.time()
    Ta8=TimeTransfer(t9-t8,T8)

    List1=Random(Omega,Size1) 
    t1=time.time()
    b2=EntGreedy(Xarray,hyper,Xab,Yab,Omega)
    b2.initializeS()
    List2,T9=b2.greedyGrow(Size1)
    b2=0
    t2=time.time()
    Ta9=TimeTransfer(t2-t1,T9)
    t2=time.time()
    b3=FishGreedy(Xarray,hyper,Xab,Yab,Omega)
    b3.initializeS()
    List3,T10=b3.greedyGrow(Size2)
    b3=0
    t3=time.time()
    Ta10=TimeTransfer(t3-t2,T10)
    t3=time.time()

    b4=CovGreedy(Xarray,hyper,Xab,Yab,Omega)
    b4.initializeS()
    List4,T11=b4.greedyGrow(Size1)
    b4=0
    t4=time.time()
    Ta11=TimeTransfer(t4-t3,T11)
    t4=time.time()
    
    b5=MutGreedy(Xarray,hyper,Xab,Yab,Omega)
    b5.initializeS()
    List5,T12=b5.greedyGrow(Size3)
    b5=0
    t5=time.time()
    Ta12=TimeTransfer(t5-t4,T12)
    
    Clist=[1.5**i for i in range(-50,50)]
    
    Xlist=[Xtest,Xval,Xctest,Xcval] 
    Ylist=[Ytest,Yval,Yctest,Ycval]  
    Aa1=AUCReturn(Xab,Yab,Xarray,Ycom,Xlist,Ylist,List1,Clist)
    Aa2=AUCReturn(Xab,Yab,Xarray,Ycom,Xlist,Ylist,List2,Clist)
    Aa3=AUCReturn(Xab,Yab,Xarray,Ycom,Xlist,Ylist,List3,Clist)
    Aa4=AUCReturn(Xab,Yab,Xarray,Ycom,Xlist,Ylist,List4,Clist)
    Aa5=AUCReturn(Xab,Yab,Xarray,Ycom,Xlist,Ylist,List5,Clist)
    Ab={}
    Ab['Random']=Aa1
    Ab['Ent']=Aa2
    Ab['Fisher']=Aa3
    Ab['Cov']=Aa4
    Ab['Mut']=Aa5
    Ab['Time']=[Ta1,Ta2,Ta3,Ta4,Ta5,Ta6,Ta7,Ta8,Ta9,Ta10,Ta11,Ta12]
    
    csts='Name'+str(int(10000*hyper))+'AUC'+str(4*ddt+fold)+str('.p')
    pickle.dump(Ab,open(csts,"wb"))
