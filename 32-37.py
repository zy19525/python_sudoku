from random import seed
from random import randint
import random
import numpy as np

def place():
    one=[]
    seed(1009)
    num=seed(randint(1,1000))
    for i in range(3):
        seed(num)
        block=[(i*3+1),(3*i+2),(3*i+3)]
        random.shuffle(block)
        one=one+block
    return one

def rowcol():
    row=place()
    col=place()
    position=list(range(9))
    sec=[]
    for n in range(3):
        for i in range(3):
            second=col[(3*i):(3*i+3)][n]
            bb=[second]
            sec=sec+bb
    for i in range(9):
        position[i]=[row[i],sec[i]]       
    return position

def test():
    full=rowcol()
    total=[]
    for i in range(6):
        fff=rowcol()
        total=full+fff
        contains=any(total.count(ele)>1 for ele in total)
        while contains:
            fff=rowcol()
            total=full+fff
            contains=any(total.count(ele)>1 for ele in total)
        full=full+fff
    return full

def matrix():
    mat = np.zeros(shape=(9,9))
    position=test()
    for n in range(63):
        mat[(position[n][0]-1),(position[n][1]-1)]=n//9+1
    return mat

def unittest(mat,r,c):
    inc=[0]
    for m in [r//3*3,r//3*3+1,r//3*3+2]:
        for n in [c//3*3,c//3*3+1,c//3*3+2]:
            inc.append(mat[m,n])
    for a in range(9):
        inc.append(mat[r,a])
        inc.append(mat[a,c])
    inc.remove(mat[r,c])
    inc.remove(mat[r,c])
    inc.remove(mat[r,c])
    return inc

def create():
    aa=False
    uu=1
    while aa==False:
        mm=matrix()
        bb=[8,9]
        random.shuffle(bb)
        ww=np.where(mm==0)
        ll=ww[1][0]
        rr=ww[1][1]
        mm[0,ll]=bb[0]
        mm[0,rr]=bb[1]
        ww=np.where(mm==0)
        for t in range(10):
            for i in range(len(ww[1])):
                remain=list(set(bb)-set(unittest(mat=mm,r=ww[0][i],c=ww[1][i])))
                if len(remain)==1:
                    mm[ww[0][i],ww[1][i]]=remain[0]
            ww=np.where(mm==0)
        if len(ww[0])==0:
            aa=True
            print(mm)
        uu=uu+1
        print(uu)
    return mm
    
def dele():
    remained=81
    origin=secc=assume=create()
    begin=81
    testt=82
    while begin!=testt:
        begin=testt
        for i in range(9):
            setall=np.where(secc==(i+1))
            length=len(setall[0])
            numbers=list(range(length))
            random.shuffle(numbers)
            for m in numbers:
                single=np.zeros(shape=(9,9))
                assume[setall[0][m],setall[1][m]]=0
                allzero=np.where(assume==0)
                lallzero=len(allzero[0])
                for n in range(lallzero):
                    single[allzero[0][n],allzero[1][n]]=1
                allgoal=np.where(assume==(i+1))
                lallgoal=len(allgoal[0])
                for a in range(lallgoal):
                    for b in [allgoal[0][a]//3*3,allgoal[0][a]//3*3+1,allgoal[0][a]//3*3+2]:
                        for c in [allgoal[1][a]//3*3,allgoal[1][a]//3*3+1,allgoal[1][a]//3*3+2]:
                            single[b,c]=0
                    single[allgoal[0][a],:]=0
                    single[:,allgoal[1][a]]=0
                for e in range(3):
                    for f in range(3):
                        small=single[(f*3):(f*3+3),(e*3):(e*3+3)]
                        aa=np.where(small==1)
                        block=set(range(9))
                        if len(set(aa[0]))==1:
                            hang=aa[0][0]+f*3
                            lie=block-set([e*3,e*3+1,e*3+2])
                            for item in lie:
                                single[hang,item]=0
                        if len(set(aa[1]))==1:
                            lie=aa[1][0]+e*3
                            hang=block-set([f*3,f*3+1,f*3+2])
                            for item in hang:
                                single[item,lie]=0
                rrr=setall[0][m]
                ccc=setall[1][m]
                rant=0
                for timer in [rrr//3*3,rrr//3*3+1,rrr//3*3+2]:
                    for timertwo in [ccc//3*3,ccc//3*3+1,ccc//3*3+2]:
                        rant=rant+single[timer,timertwo]
                if sum(single[rrr,:])==1 or sum(single[:,ccc])==1 or rant==1:
                    secc[setall[0][m],setall[1][m]]=0
                    tyt=81-len(np.where(secc==0)[1])
                    break
                assume[setall[0][m],setall[1][m]]=i+1
        testt=len(np.where(secc==0)[1])       
    print(secc)  
    print(tyt)

dele()

   
        









    



