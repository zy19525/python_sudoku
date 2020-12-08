# python_sudoku
from random import seed
from random import randint
import random
import numpy as np

def place():
    one=[]
    seed()
    for i in range(3):
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
    for i in range(7):
        contains=True
        while contains:
            fff=rowcol()
            total=full+fff
            contains=any(total.count(ele)>1 for ele in total)
        full=full+fff
        i=i+1
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
            t=t+1
        if len(ww[0])==0:
            aa=True
        uu=uu+1
        print(uu)
    return mm

def canbedected(origined,matrix,r,c):
    goal=origined[r,c]
    single=np.zeros(shape=(9,9))
    allzero=np.where(matrix==0)
    lallzero=len(allzero[0])
    for n in range(lallzero):
        single[allzero[0][n],allzero[1][n]]=1
    allgoal=np.where(matrix==goal)
    lallgoal=len(allgoal[0])
    for a in range(lallgoal):
        for b in [allgoal[0][a]//3*3,allgoal[0][a]//3*3+1,allgoal[0][a]//3*3+2]:
            for t in [allgoal[1][a]//3*3,allgoal[1][a]//3*3+1,allgoal[1][a]//3*3+2]:
                single[b,t]=0
        single[allgoal[0][a],:]=0
        single[:,allgoal[1][a]]=0
    small=np.zeros(shape=(3,3))
    for e in range(3):
        for f in range(3):
            for smallr in [f*3,f*3+1,f*3+2]:
                for smallc in [e*3,e*3+1,e*3+2]:
                    small[smallr%3,smallc%3]=single[smallr,smallc]
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
    rant=0
    for timer in [r//3*3,r//3*3+1,r//3*3+2]:
        for timertwo in [c//3*3,c//3*3+1,c//3*3+2]:
            rant=rant+single[timer,timertwo]
    if sum(single[r,:])==1 or sum(single[:,c])==1 or rant==1:
        canbedected=True
    else:
        canbedected=False
    return canbedected

    
def dele():
    assume=create()
    secc=np.zeros(shape=(9,9))
    origin=np.zeros(shape=(9,9))
    for thisway in range(9):
        for thatway in range(9):
            secc[thisway,thatway]=assume[thisway,thatway]
            origin[thisway,thatway]=assume[thisway,thatway]
    filled=0
    integer=[0]
    while filled<len(integer):
        newtime=np.where(assume!=0)
        remained=len(newtime[0])
        integer=list(range(remained))
        random.shuffle(integer)
        for integeran in integer:
            newrow=newtime[0][integeran]
            newcol=newtime[1][integeran]
            assume[newrow,newcol]=0
            stop=False
            while stop==False:
                stop=True
                thatt=np.where(assume==0)
                length=len(thatt[0])
                for one in range(length):
                    if canbedected(origined=origin,matrix=assume,r=thatt[0][one],c=thatt[1][one]):   
                        assume[thatt[0][one],thatt[1][one]]=origin[thatt[0][one],thatt[1][one]]
                        stop=False
                if stop:
                    break
            if assume[newrow,newcol]!=0:
                secc[newrow,newcol]=0
                filled=0
                for aa in range(9):
                    for bb in range(9):
                        assume[aa,bb]=secc[aa,bb]
            else:
                filled=filled+1
                for aa in range(9):
                    for bb in range(9):
                        assume[aa,bb]=secc[aa,bb]
    print(origin)
    print(assume)
    solve(matri=assume,origi=origin)
                        
def solve(matri,origi):
    aga=True
    while aga:
        zeros=np.where(matri==0)
        aga=False
        llll=len(zeros[0])
        thisrow=[]
        thiscol=[]
        for aa in range(llll):
            if canbedected(matrix=matri,origined=origi,r=zeros[0][aa],c=zeros[1][aa]):
                    rrr=zeros[0][aa]
                    ccc=zeros[1][aa]
                    thisrow.append(rrr)
                    thiscol.append(ccc)
        llen=len(thisrow)
        if llen>0:
            for lllen in range(llen):
                matri[thisrow[lllen],thiscol[lllen]]=origi[thisrow[lllen],thiscol[lllen]]
                aga=True
        print(matri)
        
dele()
