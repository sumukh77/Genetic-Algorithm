# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:11:59 2018

@author: sumuk
"""
import sys
from random import *
from string import *
from math import *
from itertools import combinations 
var=[]
ops=[]
constant=[]
rhs=0

def inp():
    global rhs
    eqn=input("Enter the equation here")
    eqn=eqn.split("=")
    lhs=eqn[0]
    rhs=eqn[1]
    c=0
    d=0
    if(lhs[0]!="-"):
            lhs="+"+lhs
    lhs=lhs+"+"
    #print(lhs)
    for i in lhs:
        #print(i)
        if(i=="+" or i=="-"):
            ops.append(i)
            #print(lhs[d+1:c])
            var.append(lhs[d+1:c])
            d=c
        c+=1
    
    for i in range(0,len(var)-1):
        if(var[i].isdigit()):
            
            rhs=int(var[i])
            del var[i]
            del ops[i-1]
    for i in range(0,len(var)-1):
        if(var[i].isalpha()):
            var[i]="1"+var[i]
    
    for i in range(1,len(var)):
        s=var[i]
        constant.append(int(s[:-1]))
        
     
    
   
inp()#calling the input function
print("the operators",ops)
print("the terms",var)
print("the constant",rhs,type(rhs))
print("the coefficents",constant)
#initializing the chromosomes
pop=6
chrom=[]
rand=[]
opt=[]
def chromo():
    global rand
    for i in range(0,pop):
        for i in range(1,len(var)):
            r=randint(-int(rhs),int(rhs))
            rand.append(r)
        #print(rand)
        chrom.append(rand)
        rand=[]
chromo()
print("the random chromosomes generated",chrom)
#evaluation obtained by using the objective function
for z in range(0,500):
    flag=0
    #global chrom
    print("the chromosomes for this generation are:",chrom)
    def objfunc(chrom):
        sum=0
        chrom_obj=[]
        for i in range(0,len(chrom)):
                ch=chrom[i]
                for j in range(1,len(var)):
                    #print(ch)
                    if(ops[j-1]=='+'):
                        sum=sum+(constant[j-1]*int(ch[j-1]))
                        #print(sum)
                    else:
                        sum=sum-(constant[j-1]*int(ch[j-1]))
                        #print(sum)
                if(sum<0):
                        sum=sum*-1
                chrom_obj.append(sum)
                sum=0
        return chrom_obj
    a=objfunc(chrom)
    print("evaluation of the chromosomes generated",a)
    for i in range(0,len(a)):
        if(a[i]==rhs):
            opt=chrom[i]
            print("the solution is obtained at generation",z,"is",opt)
            flag=1
            break
    if(flag==1):
        break
    
        
    
    fit=[]
    co=0
    cum_prob=[]
    fit_tots=0.0
    prob=[]
    def fitn():
        global fit_tots
        global co
        for i in range(0,len(a)):
            fit.append(float(1.0/(1.0+a[i])))
            fit_tots=fit_tots+fit[i]
        print("the total fitness value obtained",fit_tots)#the total fitness value obtained
        for i in fit:
            frac=i/fit_tots
            prob.append(frac)
            co=co+frac
            cum_prob.append(round(co,2))
    fitn()
    print("the cumulative probabilities",cum_prob)
    cr=[]
    new_chrom=[]
    def roulete():
        for i in range(0,pop):
                cr.append(round(uniform(0,1),3))
        #print("here",cr)
                
        
        for i in range(0,len(cr)):
            for j in range(0,len(cr)):
                if(cum_prob[j]>cr[i]):
                    new_chrom.append(chrom[j])
                    break
    roulete()
    #print(cr)
    print("the chromosomes selected for crossover",new_chrom)
    #print(chrom)
    k=0
    r=[]
    pc=0.5
    parent=[]
    comb=[]
    #print(pop)
    #print(len(new_chrom))
    while(k<pop):
            r.append(round(uniform(0,1),3))
            #print(r[k])
            if(r[k]<pc):
                parent.append(new_chrom[k])
                #del new_chrom[k]
            k=k+1
            #print("k",k)
            #print(r)
    
    print("the parents obtained",parent)
    #parent=[[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
    if(len(parent)>1):
        i=0
        while(i<(len(parent)-1)):
            if(i==len(parent)-1):
                comb.append([parent[i],parent[0]])
            comb.append([parent[i],parent[i+1]])
            i=i+1
            
    print("the various combinations",comb)
    r=[]
    for i in range(0,len(parent)):
        r.append(randint(1,(len(new_chrom[0])-2)))
    #print(r)
    
    new_par=[]
    #print(comb)
    for i in range(0,len(parent)-1):   #had to put -1 here
        #print(i)
        p1=comb[i][0]
        p2=comb[i][1]
        new_par.append(p1[:r[i]]+p2[r[i]:])
    print("the new parents obtained after crossover",new_par)
    #print(new_chrom)
    for i in range(len(new_par),len(new_chrom)):
        new_par.append(new_chrom[i])
    #print(new_par)
    tots_gen=pop*(len(new_chrom[0]))
    mutation_var=0.1
    num_mut=int(mutation_var*tots_gen)
    print("the number of chromosomes to be mutated:",num_mut)
    
    
    
    
    r=0
    mut_par=[]
    final_chrom=[]
    def mutate():
        for i in new_par:
            mut_par.extend(i)
        #print(mut_par)
        for i in range(0,num_mut):
            ri=randint(0,tots_gen)
            r1=randint(-int(rhs),int(rhs))
            mut_par[ri-1]=r1
        #print(mut_par)
        fc=[]
        
        j=0
        len_chrom=len(new_chrom[0])
        for i in range(len_chrom,len(mut_par)+len_chrom,len_chrom):
            fc=mut_par[j:i]
            j=i
            final_chrom.append(fc)
        print("the chromosomes obtained after a generation are:",final_chrom)
        print("----------------x----------x-------------x-------------x-----------x----------------")
        #print(z)
        
    chrom=final_chrom
    mutate()
        