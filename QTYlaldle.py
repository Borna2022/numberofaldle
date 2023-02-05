import numpy as np
import math
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
ladlesfree=["L1","L2","L3","L4","L5","L6"]
ladlemeltin=[]
c3=[]


l1free,l2free,l3free,l4free,l5free,l6free=0,0,0,0,0,0

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

for j in range(len(ladlesfree)):
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

print("ladle free: ", ladlesfree)
print("ladle melt in: ", ladlemeltin[:numbe_of_heat])
print("ladle free time: ", ladlefreetime[:numbe_of_heat])
print ("tap:1 ",endeaf)
print("==================================================================================")
print ("tap: ",endeaf)
print ("end ccm: ", endccm[:numbe_of_heat])
print("==================================================================================")
print("start cast: ", startcast)
print("==================================================================================")
print ("start: ",starteaf)
print ("start lf: ", startlf[:numbe_of_heat])
print ("end lf: ", endlf[:numbe_of_heat])
print ("start ccm: ", startccm[:numbe_of_heat])
print("Sequence #1: ", a)
print("Sequence #2:", b)
print("Sequence #3:", c)
print("Sequence #4:", d)
print("Sequence #5:", f)





    
