from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import roc_auc_score



def AppendY(Xm,Ym):
    n,d=np.shape(Xm)
    Xa=np.concatenate((Xm,np.zeros((1,d))),0)
    if Ym[0]==1:
        Ya=np.concatenate((Ym,np.array([-1])))
    else:
        Ya=np.concatenate((Ym,np.array([1])))
    return Xa,Ya 


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
