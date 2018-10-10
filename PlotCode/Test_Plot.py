
import numpy as np
import pickle 
import matplotlib.pyplot as plt




def SizePlot(MeanList,ErrList,TM,Title,Name):#LocList,TitleList):
    
    fig,ax=plt.subplots(1,3,figsize=(32,10)) 

    string10=str('Random')
    string11=str('D-NG')
    string12=str('D-FLP')
    string13=str('D-SLP')
    string14=str('Ent')
    string15=str('Fisher')
    string16=str('Mut')

    AM1=MeanList[0]
    AM2=MeanList[1]
    Er1=ErrList[0]
    Er2=ErrList[1]
    ax[0].plot(np.arange(1,len(AM1[0])+1), np.array(AM1[0]) , 'ro', markersize=10,markevery=8, linestyle=':')
    ax[0].plot(np.arange(1,len(AM1[1])+1), np.array(AM1[1]) , 'bv',markersize=10, markevery=8, linestyle=':')
    ax[0].plot(np.arange(1,len(AM1[2])+1), np.array(AM1[2]) , 'y1', markersize=10,markevery=8, linestyle=':')
    ax[0].plot(np.arange(1,len(AM1[3])+1), np.array(AM1[3]) , 'g8',markersize=10, markevery=8, linestyle=':')
    ax[0].plot(np.arange(1,len(AM1[4])+1), np.array(AM1[4]) , 'mp', markersize=10,markevery=8, linestyle=':')
    
    
    ax[1].plot(np.arange(1,len(AM2[0])+1), np.array(AM2[0]) , 'ro', markersize=10,markevery=8, linestyle=':')
    ax[1].plot(np.arange(1,len(AM2[1])+1), np.array(AM2[1]) , 'bv',markersize=10, markevery=8, linestyle=':')
    ax[1].plot(np.arange(1,len(AM2[2])+1), np.array(AM2[2]) , 'y1', markersize=10,markevery=8, linestyle=':')
    ax[1].plot(np.arange(1,len(AM2[3])+1), np.array(AM2[3]) , 'g8',markersize=10, markevery=8, linestyle=':')
    ax[1].plot(np.arange(1,len(AM2[4])+1), np.array(AM2[4]) , 'mp', markersize=10,markevery=8, linestyle=':')
    
    
    
    
    ax[0].fill_between(np.arange(1,len(AM1[0])+1), AM1[0]-Er1[0], AM1[0]+Er1[0],alpha=0.2, edgecolor='r', facecolor='r')
    ax[0].fill_between(np.arange(1,len(AM1[1])+1), AM1[1]-Er1[1], AM1[1]+Er1[1],alpha=0.2, edgecolor='b', facecolor='b')
    ax[0].fill_between(np.arange(1,len(AM1[2])+1), AM1[2]-Er1[2], AM1[2]+Er1[2],alpha=0.2, edgecolor='y', facecolor='y')
    ax[0].fill_between(np.arange(1,len(AM1[3])+1), AM1[3]-Er1[3], AM1[3]+Er1[3],alpha=0.2, edgecolor='g', facecolor='g')
    ax[0].fill_between(np.arange(1,len(AM1[4])+1), AM1[4]-Er1[4], AM1[4]+Er1[4],alpha=0.2, edgecolor='m', facecolor='m')
    
    ax[1].fill_between(np.arange(1,len(AM2[0])+1), AM2[0]-Er2[0], AM2[0]+Er2[0],alpha=0.2, edgecolor='r', facecolor='r')
    ax[1].fill_between(np.arange(1,len(AM2[1])+1), AM2[1]-Er2[1], AM2[1]+Er2[1],alpha=0.2, edgecolor='b', facecolor='b')
    ax[1].fill_between(np.arange(1,len(AM2[2])+1), AM2[2]-Er2[2], AM2[2]+Er2[2],alpha=0.2, edgecolor='y', facecolor='y')
    ax[1].fill_between(np.arange(1,len(AM2[3])+1), AM2[3]-Er2[3], AM2[3]+Er2[3],alpha=0.2, edgecolor='g', facecolor='g')
    ax[1].fill_between(np.arange(1,len(AM2[4])+1), AM2[4]-Er2[4], AM2[4]+Er2[4],alpha=0.2, edgecolor='m', facecolor='m')
    
    ax[2].plot(np.arange(1,len(TM[0])+1), np.array(TM[0]) , 'ro', markersize=10,markevery=8, linestyle=':', label=string11)
    ax[2].plot(np.arange(1,len(TM[1])+1), np.array(TM[1]) , 'c+', markersize=10,markevery=8, linestyle=':', label=string12)
    ax[2].plot(np.arange(1,len(TM[2])+1), np.array(TM[2]) , 'kx',markersize=10, markevery=8, linestyle=':',label=string13)
    ax[2].plot(np.arange(1,len(TM[3])+1), np.array(TM[3]) , 'bv',markersize=10, markevery=8, linestyle=':',label=string14)
    ax[2].plot(np.arange(1,len(TM[4])+1), np.array(TM[4]) , 'y1', markersize=10,markevery=8, linestyle=':', label=string15)
    ax[2].plot(np.arange(1,len(TM[5])+1), np.array(TM[5]) , 'g8',markersize=10, markevery=8, linestyle=':',label=string16)
    ax[2].plot(np.array([0,0.00001]), np.array([0,0.00001]) , 'mp', markersize=10, markevery=8, linestyle=':', label=string10)
    
    
    
  
    
    
    
    
    ax[0].set_ylabel('Absolute Prediction AUC',fontsize=30)
    ax[1].set_ylabel('Comparison Prediction AUC',fontsize=30)
    ax[2].set_ylabel('Computation Time',fontsize=30)
    ax[0].set_xlabel('Batch Size K',fontsize=30)
    ax[1].set_xlabel('Batch Size K',fontsize=30)
    ax[2].set_xlabel('Batch Size K',fontsize=30)
    ax[0].set_ylim([0.61, 0.92])
    ax[1].set_ylim([0.61, 0.92])

    ax[0].xaxis.set_tick_params(labelsize=25)
    ax[0].yaxis.set_tick_params(labelsize=25)
    ax[0].yaxis.tick_right()
    ax[1].xaxis.set_tick_params(labelsize=25)
    ax[1].yaxis.set_tick_params(labelsize=25)
    ax[1].yaxis.tick_right()
    ax[2].xaxis.set_tick_params(labelsize=25)
    ax[2].yaxis.set_tick_params(labelsize=25) 
    ax[2].set_yscale('log')
    ax[2].set_ylabel('Time $(s)$',fontsize=30)    
    ax[2].yaxis.tick_right()
    

    ax[2].legend(loc=4,markerscale=1.,prop={'size':20})
    
    fig.suptitle(Title, y=0.94, fontsize=35)
    
    fig.savefig(Name+'.pdf', bbox_inches='tight', pad_inches=0) 




