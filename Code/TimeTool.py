def TimeTransfer(timetotal,Timelist):
    Time=[]
    for i in range(len(Timelist)):
        Time.append(timetotal)
        timetotal-=Timelist[-i-1]
    TimeR=Time.reverse()
    Ta=np.array(Time)
    return Ta
