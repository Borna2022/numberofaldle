import numpy as np
import math
import matplotlib.pyplot as plt

stt=int(input("please enter start to tap: "))
preptime=int(input("please enter prep time: "))
casttime=int(input("please enter cast time: "))
lftime=int(input("please enter lf time: "))
numberofsequence=int(input("please enter number of sequence: "))
trftolf=int(20)
trftoccm=int(10)
trfoneafladlecar=int(10)
laldlepreptime=int(60)
waitonccm=int(20)
rotatelaldle=int(2)
ccmpreptime=int(60)

difftapeaf=preptime+trftolf+lftime+trftoccm+waitonccm+rotatelaldle

qtyseq=round(1440/(numberofsequence*casttime))
needeaf=round((stt+preptime)/casttime,ndigits=2)

print("number of sequence: ",qtyseq)
print("need of eaf:",needeaf)
print ("trf to lf",trftolf,"trf to ccm",trftoccm,"trf on eaf ladle car",trfoneafladlecar,
       "laldle prep time",laldlepreptime,"wait on ccm",waitonccm,"rotate laldle",rotatelaldle,
       "ccm prep time",ccmpreptime)
print("==================================================================================")

numbe_of_heat=round(1440/(stt+preptime))
starteaf=[]
endeaf=[]
startlf=[]
endlf=[]
startccm=[]
endccm=[]
ladlefreetime=[]
laldlesheat=[]
ladlesfree=["L1","L2","L3","L4","L5","L6","L7","L8","L9","L10","L11","L12","L13","L14","L15",
            "L16","L17","L18","L19","L20","L21","L22"]
ladlemeltin=[]
c3=[]

indexcounter=1

for i in range(stt,1440):   
    if i % (stt)==0:    
        endeaf.append(i-preptime)
        starteaf.append(i-stt)
        startlf.append(i+trftolf)    
        endlf.append(i+trftolf+lftime)        
        indexcounter +=1
        
startcast=endlf[0]+trftoccm+waitonccm

for i in range(startcast,1440):
     if i % (casttime)==0:
         startccm.append(i+rotatelaldle)
         endccm.append(i+casttime)
for i in endccm:
         ladlefreetime.append(i+laldlepreptime)

for x in ladlesfree:
    if x not in ladlemeltin:
        c3.append(x)
        ladlesfree=c3

for i in range(numberofsequence,len(endccm)):
    if i %numberofsequence !=0:
        endccm[i]=endccm[i-1]+casttime
    if i%numberofsequence==0:
        endccm[i]=endccm[i-1]+ccmpreptime+casttime
        

print(len(ladlesfree))
print(len(endeaf))
lenladlefre=len(endeaf)
for j in range(lenladlefre):
    for k in range(len(endeaf)):
        if endeaf[k]<=ladlefreetime[j]:
            ladlemeltin.append(ladlesfree[k])
        else:   
            break
a=[]
b=[]
c=[]
d=[]
f=[]
a=endccm[0:numberofsequence]
b=endccm[numberofsequence:numberofsequence*2]    
c=endccm[numberofsequence*2:numberofsequence*3]    
d=endccm[numberofsequence*3:numberofsequence*4]
f=endccm[numberofsequence*4:numberofsequence*5]
######################################################
print("ladle free: ", ladlesfree)
print("ladle melt in: ", ladlemeltin)
print("ladle free time: ", ladlefreetime)
print ("tap:1 ",endeaf)
print("==================================================================================")
print ("tap: ",endeaf)
print ("end ccm: ", endccm)
print("==================================================================================")
print("start cast: ", startcast)
print("==================================================================================")
print ("start: ",starteaf)
print ("start lf: ",startlf)
print ("end lf: ",endlf)
print ("start ccm: ",startccm)
print("Sequence #1:", a)
print("Sequence #2:", b)
print("Sequence #3:", c)
print("Sequence #4:", d)
print("Sequence #5:", f)

########################################################
xstend=[]
for i in range(stt,1440):   
    if i % (stt)==0:
        xstend.append(i-stt)
        xstend.append(i-preptime)
print(xstend)
ystend=[]

for i in range (len(xstend)):
    ystend.append(150)
counter=1
for i in starteaf:
    plt.annotate(f"{counter}",xy=(i,151),size=5)
    counter+=1
plt.plot(xstend, ystend,marker="|")


########################################### a
xa= a
xa.insert(0,startccm[0])
#print("xa:",xa,len(xa))
ya=[]
tapscheaf=[]
startscheaf=[]
lista=[]

for i in range (len(xa)):
    ya.append(100)
    tapscheaf.append(xa[i]-difftapeaf)
    startscheaf.append(tapscheaf[i]-stt)
    lista.append(startscheaf[i])
    lista.append(tapscheaf[i])
#print ("startscheaf:",startscheaf,)
print("lista:",lista)
plt.plot(xa, ya ,  marker="|")
texta=[]
for i in range(0,numberofsequence):
    plt.annotate(f'{ladlemeltin[i]}', xy=(xa[i], 100),size=7)
    texta.append(ladlemeltin[i])
print("text a",texta)
for i in range(1,len(xa)):
    plt.annotate(f'{i}', xy=(xa[i]-casttime, 98),size=7)
    
x=lista
y1 = [140 if i%4 < 2 else 138 for i in range(len(lista))]

print(y1)

plt.plot(x[0:2],y1[0:2],marker="|")    #1
plt.plot(x[2:4],y1[2:4],marker="|")    #2
plt.plot(x[4:6],y1[4:6],marker="|")    #3
plt.plot(x[6:8],y1[6:8],marker="|")    #4
plt.plot(x[8:10],y1[8:10],marker="|")  #5
plt.plot(x[10:12],y1[10:12],marker="|")#6
plt.plot(x[12:14],y1[12:14],marker="|")#7
plt.plot(x[14:16],y1[14:16],marker="|")#8
plt.plot(x[16:18],y1[16:18],marker="|")#9
plt.plot(x[18:20],y1[18:20],marker="|")#10
plt.plot(x[20:22],y1[20:22],marker="|")#11
plt.plot(x[22:24],y1[22:24],marker="|")#12
plt.plot(x[24:26],y1[24:26],marker="|")#13
plt.plot(x[26:28],y1[26:28],marker="|")#14



###################################################### b
xb= b
xb.insert(0,xb[0]-casttime)
#print("xb:",xb)
yb=[]
tapscheaf=[]
startscheaf=[]
listb=[]
for i in range (len(xb)):
    yb.append(100)
    tapscheaf.append(xb[i]-difftapeaf)
    startscheaf.append(tapscheaf[i]-stt)
    listb.append(startscheaf[i])
    listb.append(tapscheaf[i])
#print ("startscheaf:",startscheaf,"tapscheaf:",tapscheaf)
print("listb:",listb)
plt.plot(xb, yb ,  marker="|")
textb=[]
textb=ladlemeltin[numberofsequence:numberofsequence*2]
for i in range(0,numberofsequence):
    plt.annotate(f'{textb[i]}', xy=(xb[i], 100),size=7)
print("text b",textb)
lastindexa = len(xa) - 1
print("lastindexa:",lastindexa)
for i in range(1,len(xb)):
    plt.annotate(f'{i+lastindexa}', xy=(xb[i]-casttime, 98),size=7)

x=listb
y1 = [140 if i%4 < 2 else 138 for i in range(len(listb))]

print(y1)

plt.plot(x[0:2],y1[0:2],marker="|")    #1
plt.plot(x[2:4],y1[2:4],marker="|")    #2
plt.plot(x[4:6],y1[4:6],marker="|")    #3
plt.plot(x[6:8],y1[6:8],marker="|")    #4
plt.plot(x[8:10],y1[8:10],marker="|")  #5
plt.plot(x[10:12],y1[10:12],marker="|")#6
plt.plot(x[12:14],y1[12:14],marker="|")#7
plt.plot(x[14:16],y1[14:16],marker="|")#8
plt.plot(x[16:18],y1[16:18],marker="|")#9
plt.plot(x[18:20],y1[18:20],marker="|")#10
plt.plot(x[20:22],y1[20:22],marker="|")#11
plt.plot(x[22:24],y1[22:24],marker="|")#12
plt.plot(x[24:26],y1[24:26],marker="|")#13
plt.plot(x[26:28],y1[26:28],marker="|")#14


###################################################### c
xc= c
if len(xc) != 0:
    xc.insert(0,xc[0]-casttime)
    #print("xc:",xc)
    yc=[]
    tapscheaf=[]
    startscheaf=[]
    listc=[]
    for i in range (len(xc)):
        yc.append(100)
        tapscheaf.append(xc[i]-difftapeaf)
        startscheaf.append(tapscheaf[i]-stt)
        listc.append(startscheaf[i])
        listc.append(tapscheaf[i])
    #print ("startscheaf:",startscheaf,"tapscheaf:",tapscheaf)
    print("listc:",listc)
    plt.plot(xc, yc ,  marker="|")
    textc=[]
    textc=ladlemeltin[numberofsequence*2:numberofsequence*3]
    print("textc:",textc)
    print("xc:",xc)
    print (len(textc))
    for i in range(0,len(xc)):
        if len(xc)>len(textc):
            break
        else:
            plt.annotate(f'{textc[i]}', xy=(xc[i], 100),size=7)
    print("text c",textc)
    lastindexb = (len(xa)-1)*2
    print("lastindexb:",lastindexa)
    for i in range(1,len(xc)):
        plt.annotate(f'{i+lastindexb}', xy=(xc[i]-casttime, 98),size=7)

    x=listc
    y1 = [140 if i%4 < 2 else 138 for i in range(len(listc))]

    print(y1)

    plt.plot(x[0:2],y1[0:2],marker="|")    #1
    plt.plot(x[2:4],y1[2:4],marker="|")    #2
    plt.plot(x[4:6],y1[4:6],marker="|")    #3
    plt.plot(x[6:8],y1[6:8],marker="|")    #4
    plt.plot(x[8:10],y1[8:10],marker="|")  #5
    plt.plot(x[10:12],y1[10:12],marker="|")#6
    plt.plot(x[12:14],y1[12:14],marker="|")#7
    plt.plot(x[14:16],y1[14:16],marker="|")#8
    plt.plot(x[16:18],y1[16:18],marker="|")#9
    plt.plot(x[18:20],y1[18:20],marker="|")#10
    plt.plot(x[20:22],y1[20:22],marker="|")#11
    plt.plot(x[22:24],y1[22:24],marker="|")#12
    plt.plot(x[24:26],y1[24:26],marker="|")#13
    plt.plot(x[26:28],y1[26:28],marker="|")#14

###################################################### d
xd= d
if len(xd) != 0:
    print("xd:",xd)
    xd.insert(0,xd[0]-casttime)
    #print("xd:",xd)
    yd=[]
    tapscheaf=[]
    startscheaf=[]
    listd=[]
    for i in range (len(xd)):
        yd.append(100)
        tapscheaf.append(xd[i]-difftapeaf)
        startscheaf.append(tapscheaf[i]-stt)
        listd.append(startscheaf[i])
        listd.append(tapscheaf[i])
    #print ("startscheaf:",startscheaf,"tapscheaf:",tapscheaf)
    print("listd:",listd)    

    plt.plot(xd, yd ,  marker="|")
    textd=[]
    textd=ladlemeltin[numberofsequence*3:numberofsequence*4]
    print (len(textd))
    print("text d",textd)

    for i in range(0,len(xd)):
        plt.annotate(f'{textd[i]}', xy=(xd[i], 100),size=7)
    print("text d",textd)
    lastindexc = (len(xa)-1)*3
    print("lastindexc:",lastindexa)
    for i in range(1,len(xd)):
        plt.annotate(f'{i+lastindexc}', xy=(xd[i]-casttime, 98),size=7)

    x=listd
    y1 = [140 if i%4 < 2 else 138 for i in range(len(listd))]

    print(y1)

    plt.plot(x[0:2],y1[0:2],marker="|")    #1
    plt.plot(x[2:4],y1[2:4],marker="|")    #2
    plt.plot(x[4:6],y1[4:6],marker="|")    #3
    plt.plot(x[6:8],y1[6:8],marker="|")    #4
    plt.plot(x[8:10],y1[8:10],marker="|")  #5
    plt.plot(x[10:12],y1[10:12],marker="|")#6
    plt.plot(x[12:14],y1[12:14],marker="|")#7
    plt.plot(x[14:16],y1[14:16],marker="|")#8
    plt.plot(x[16:18],y1[16:18],marker="|")#9
    plt.plot(x[18:20],y1[18:20],marker="|")#10
    plt.plot(x[20:22],y1[20:22],marker="|")#11
    plt.plot(x[22:24],y1[22:24],marker="|")#12
    plt.plot(x[24:26],y1[24:26],marker="|")#13
    plt.plot(x[26:28],y1[26:28],marker="|")#14


######################################################
listall=lista+listb+listc+listd
x=listall
print(listall)
y1 = [140 if i%4 < 2 else 138 for i in range(len(listall))] 
y2 = [142 if i%4 < 2 else 136 for i in range(len(listall))] 
c=0
for i in range(len(listall)):
    if i%2 ==0:
        c+=1
        plt.annotate(f'{c}', xy=(listall[i], y1[i]),size=7)
tapscheduled=[]
for i in range(1,len(listall),2):
        plt.annotate(f'{listall[i]}', xy=(listall[i], y2[i]),size=6)
        tapscheduled.append(listall[i])
        
print(min(len(tapscheduled),len(endccm),len(ladlefreetime)))
minlen=min(len(tapscheduled),len(endccm),len(ladlefreetime))
for i in range(minlen):
    print("ID:",i+1," tapscheduled:",tapscheduled[i],"end cast",endccm[i],"ladlefreetime",ladlefreetime[i])
c=0
for i in range(minlen):
    for j in range(minlen):
        if tapscheduled[i]< ladlefreetime[j]:
            c+=1
            print(i,j,c)
            break 
  
            
    
    

plt.show()
