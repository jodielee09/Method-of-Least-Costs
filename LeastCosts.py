# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:21:23 2019

@author: jodie
"""
import numpy as np

def find(target,ToSearch):
    x=[(i, t.index(target))
    for i, t in enumerate(ToSearch)
    if target in t]
    return x

def MatMin(supplyinfo,demandinfo,costinfo):
    C=np.matrix(costinfo.copy())
    sn=len(supplyinfo)
    dn=len(demandinfo)
    sol=np.zeros((sn,dn))
    costs=list(costinfo)
    supply=supplyinfo.copy()
    demand=demandinfo.copy()
    count=0
    while (sum(supply)+sum(demand)) != 0 and count<20:
        count=count+1
        Min=[]
        for a in range(sn):
            row=costs[a]
            Row=[]
            for b in range(dn):
                if type(row[b])==int:
                    Row.append(row[b])
                 
                if b==dn-1 and len(Row)<=0:
                    continue
                if b==dn-1:
                    Min.append(min(Row))
        if len(Min)==0:
            return sol
        smallest=min(Min)
        location=find(smallest,costs)
        if len(location)==1: 
            location=find(smallest,costs)[0]
            costs[location[0]][location[1]]='x'
            if supply[location[0]]>=demand[location[1]]:   
                sol[location[0]][location[1]]=demand[location[1]]
                demand[location[0]]=supply[location[0]]-demand[location[1]]
                demand[location[1]]=0
            else:
                sol[location[0]][location[1]]=supply[location[0]]
                demand[location[1]]=demand[location[1]]-supply[location[0]]
                supply[location[0]]=0 
                
        else: 
            locations=find(smallest,costs)
            l=len(locations)
            m=[]
            for a in range(l):
                L=locations[a]
                s=L[1]
                d=L[0]
                if s>=d:
                    m.append(s)
                else:
                    m.append(d)
            M=max(m)
            loc=m.index(M)
            location=locations[loc]
            costs[location[0]][location[1]]='x'
            if supply[location[0]]>=demand[location[1]]:                
                sol[location[0]][location[1]]=demand[location[1]]
                supply[location[0]]=supply[location[0]]-demand[location[1]]
                demand[location[1]]=0     

            else:
                sol[location[0]][location[1]]=supply[location[0]]
                demand[location[1]]=demand[location[1]]-supply[location[0]]
                supply[location[0]]=0 

    feasabilitytest=np.count_nonzero(sol)
    print('Number of stepping stones =', feasabilitytest)
    if feasabilitytest==(sn+dn-1):
        print('Feasibility test passed')
    print(sol)
    z=0
    for k in range(sn):
        for l in range(dn):
            z=z+C[k,l]*sol[k,l]
    print('Cost is £', int(z),'for this solution.')
                
                

costs=[[10,12,13,8,14,19],[15,18,12,16,19,20],[17,16,13,14,10,18],[19,18,20,21,12,13]]
MatMin([18,22,39,14],[10,11,13,20,24,15],costs)