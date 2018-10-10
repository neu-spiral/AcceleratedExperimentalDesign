



import matplotlib.pyplot as plt  
import numpy as np  


import re



from Greedypack import *


def AllData_Bar(TimeM,TimeS,N, Name):
    
    N = 7
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.13       # the width of the bars
    widthlist=[width*(i-1) for i in range(8)]
    
    
    colorlist=[ 'orange', 'm', 'y' ,'k' ,'b' ,'r' ,'c']
    relist=[]
    hatchmap = [ '/', '\\', '\\\\', '-', '--', '+', '']
    meanlist=[np.arange(7)/7 for i in range(8)]
    fig, ax = plt.subplots(figsize=(4*3,3))
    
    for i in range(7):
        re = ax.bar(ind+widthlist[i+1], Amean[:,i+1],width,yerr=menStd[:,i+1], color=colorlist[i],hatch=hatchmap[i], log=True)
        #ax.set_yscale('log')
        relist.append(re)
    # add some text for labels, title and axes ticks
    
    ax.set_xlim(-0.1,6.9)
    ax.set_ylim(0.001,1)
    ax.yaxis.tick_right()
    ax.set_ylabel('Normalized Time', fontsize=20)
    ax.xaxis.set_tick_params(labelsize=20)
    ax.yaxis.set_tick_params(labelsize=20)
    #ax.set_title('Execution Time For Algorithms')
    ax.set_xticks(ind + width*3)
    ax.set_xticklabels(('ROP', 'Netflix', 'Sushi', 'Camra', 'ROP5K', 'SIFT', 'MSLR'),fontsize=20)
    
    
    ax.legend((relist[0][0],relist[1][0],relist[2][0],relist[3][0],relist[4][0],relist[5][0],relist[6][0]),( 'FG','SG', 'NL','FLP', 'FLM', 'SLP','SLM'),bbox_to_anchor=(0., 1.02, 1., .102),mode='expand',ncol=8,fontsize=16,borderaxespad=0.)
    c2='AllPlot7'
    fig.savefig(c2+'.pdf', bbox_inches='tight', pad_inches=0)
