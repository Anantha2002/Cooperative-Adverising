import numpy as np
import math
from operator import add
# A manufacturers national advertising level
"""ai|ij the retailer 1s local advertising level in advertising
option i for pair (i,j)"""
"""bi|ij the retailer 2s local advertising level in advertising
option i for pair (i,j)"""
"""t1ij the participation rate of manufacturer in 
retailer 1s advertising for pair (i,j)"""
"""t2ij theparticipation rate of manufacturer in retailer 2s advertising 
for pair (i,j)"""

#Function to calculate the NASH EQUILIBRIUM
def nashEqu(l1):
    row_play=[]
    col_play=[]
    for i in range(0,2):
        if i==0:
            temp=max(l1[i][1],l1[i+1][1])
            if temp==l1[i][1]:
                row_play.append([i,0])
            else:
                row_play.append([i+1,1])
        elif i==1:
            temp=max(l1[i+1][1],l1[i+2][1])
            if temp==l1[i+1][1]:
                row_play.append([i,1])
            else:
                row_play.append([i+1,2])
    for j in range(0,2):
        if j==0:
            temp=max(l1[j][0],l1[j+1][0])
            if temp==l1[j][0]:
                col_play.append([j,0])
            else:
                col_play.append([j+1,0])
        elif j==1:
            temp=max(l1[j+1][0],l1[j+2][0])
            if temp==l1[j+1][0]:
                col_play.append([j,0])
            else:
                col_play.append([j+1,0])
    for i in range(0,2):
        for j in range(0,2):
            if row_play[i]==col_play[j]:
                return [i,j]

#Function to Calculate the a value
def a(i,eta,c=1):
    n=eta
    if c==1:
        if i==1:
            ki=k1
            ci=c1
            ai=math.pow(((rho1*n*ki)/(2*ci)),2)
        else:
            ki=k2
            ci=c2
            ai=math.pow(((rho1*n*ki)/(2*ci)),2)
    else:
        if i==1:
            ki=k1
            ci=c1
            ai=((ki/(4*ci))*(2*rhom+rho1*n))**2
        else:
            ki=k2
            ci=c2
            ai=((ki/(4*ci))*(2*rhom+rho1*n))**2
    return ai
#(rho1*n*ki)/(2*ci)
#(rho2*(1-n)*kj)/(2*cj)

#Function to calculate the b value
def b(i,eta,c=1):
    n=eta
    if c==1:
        if i==1:
            kj=k1
            cj=c1
            bj=math.pow(((rho2*(1-n)*kj)/(2*cj)),2)
        else:
            kj=k2
            cj=c2
            bj=math.pow(((rho2*(1-n)*kj)/(2*cj)),2)
    else:
        if i==1:
            kj=k1
            cj=c1
            bj=((kj/(4*cj))*(2*rhom+rho2*(1-n)))**2
        else:
            kj=k2
            cj=c2
            bj=((kj/(4*cj))*(2*rhom+rho2*(1-n)))**2
    return bj

#Function to find the Profit of Manufacturer
def PIM(i,j):
    if i==1:
        ki=k1
        kj=k2
        ai=a(i)
        bj=b(j)
        ci=c1
        cj=c2
        pim=rhom*(ki*(math.pow(ai,0.5))+kj*(math.pow(bj,0.5))+km*(math.pow(A,0.5)))-t1*ci*ai-t2*cj*bj-C*A
    else:
        ki=k2
        kj=k1
        ai=a(i)
        bj=b(j)
        ci=c2
        cj=c1
        pim=rhom*(ki*(math.pow(ai,0.5))+kj*(math.pow(bj,0.5))+km*(math.pow(A,0.5)))-t1*ci*ai-t2*cj*bj-C*A
    return pim

#Function to find the Profit of Retailer 1
def PI1(i,j,eta,c=1):
    n=float(eta)
    temp=c
    #print(i,j)
    if i==1:
        ai=a(i,n,c=temp)
        bj=b(j,n,c=temp)
        ci=c1
        ki=k1
        kj=k2
        # print("kj:",kj)
        # print("bj:",bj)
        tempA=ki*(ai**0.5)
        tempB=kj*(bj**0.5)
        tempC=km*(A**0.5)
        tempD=tempA+tempB+tempC
        tempE=rho1*n
        # print(tempA,tempB,tempC,tempD,tempE)
        # print("RHO1:",rho1,"\t",n)
        temp1=rho1*n*tempD
        #temp2=int((1-t1))*ci*ai
        # print("The value of temp is:",temp1)
        # print("TEmp2:",temp2)
        #pro1*n*((k1*((a1ij)**0.5))+(k2*((b2ij)**0.5))+(km*((A)**0.5)))-(1-t1ij)*c1*a1ij
        pi1=rho1*n*((ki*((ai)**0.5))+(kj*((bj)**0.5))+(km*((A)**0.5)))-(1-t1)*ci*ai
# ki*math.pow(ai,0.5)
    else:
        ai=a(i,n,c=temp)
        bj=b(j,n,c=temp)
        ci=c2
        ki=k2
        kj=k1
        # print("kj:",kj)
        # print("bj:",bj)
        tempA=ki*(ai**0.5)
        tempB=kj*(bj**0.5)
        tempC=km*(A**0.5)
        tempD=tempA+tempB+tempC
        tempE=rho1*n
        # print(tempA,tempB,tempC,tempD,tempE)
        # print("RHO1:",rho1,"\t",n)
        temp1=rho1*n*tempD
        #temp2=(1-t1)*ci*ai
        # print("The value of temp is:",temp1)
        # print("TEmp2:",temp2)
        pi1=rho1*n*((ki*((ai)**0.5))+(kj*((bj)**0.5))+(km*((A)**0.5)))-(1-t1)*ci*ai
    return int(pi1)

#Function to find the Profit of Retailer 2
def PI2(i,j,eta,c=1):
    temp=c
    n=int(eta)
    #print(i,j)
    if i==1:
        ai=a(i,n,c=temp)
        bj=b(j,n,c=temp)
        cj=c2
        ki=k1
        kj=k2
        #profit = pro2*(1-n)*((k1*((a1ij)**0.5))+(k2*((b2ij)**0.5))+(km*((A)**0.5)))-(1-t2ij)*c2*b2ij
        pi2=rho2*(1-n)*((ki*((ai)**0.5))+(kj*((bj)**0.5))+(km*((A)**0.5)))-(1-t2)*cj*bj
    else:
        ai=a(i,n,c=temp)
        bj=b(j,n,c=temp)
        cj=c1
        ki=k2
        kj=k1
        pi2=rho2*(1-n)*((ki*((ai)**0.5))+(kj*((bj)**0.5))+(km*((A)**0.5)))-(1-t2)*cj*bj
    return int(pi2)

#Function to find the Profit Matrix
def funMatrix(eta,c=1):
    temp=C
    n0=float(eta)
    l1=[]
    matrix1=[]
    for i in range(0,2):
        for j in range(0,2):
            if i==j:
                l1.append(PI1(i+1,j+1,0.5,temp))
                l1.append(PI2(i+1,j+1,0.5,temp))
                matrix1.append(l1)
            else:
                l1.append(PI1(i+1,j+1,n0))
                l1.append(PI2(i+1,j+1,float(1-n0)))
                matrix1.append(l1)
            #matrix[i][j]=l1
            l1=[]
    return matrix1
#stage2

#THE MAIN FUNCTION STARTS FROM HERE
f=open("stage1.txt",'r')
lines=f.read()
lines=lines.split()
#print(lines)
rhom=float(lines[0])
rho1=float(lines[1])
rho2=float(lines[2])
km=float(lines[3])
k1=float(lines[4])
k2=float(lines[5])
C=float(lines[6])
c1=float(lines[7])
c2=float(lines[8])
f.close()
n0=0.43
A=math.pow(((rhom*km)/(2*C)),2)
t1=(2*rhom-rho1*n0)/(2*rhom+rho1*n0)
#print(t1)
t2=(2*rhom-rho2*(1-n0))/(2*rhom+rho2*(1-n0))
# print(t2)
# print(A)
# print(a(1))
# print(b(1))
# l1=[]
print("Enter 1 to calculate the profit without cooperative deal")
print("Enter 2 to calculate the profit with cooperative deal")
#choice=int(input("Enter your choice:"))
choice=1
#n2=float(input("Enter the expected market share in 2nd stage:"))
n2=0.43
#n1=float(input("Enter the expected reduced market share in 2nd stage:"))
n1=0.41
#n3=float(input("Enter the expected increased market sharein 2nd stage:"))
n3=0.45
matrix1=funMatrix(n1,choice)
matrix2=funMatrix(n2,choice)
matrix3=funMatrix(n3,choice)
nash1=nashEqu(matrix1)
nash2=nashEqu(matrix2)
nash3=nashEqu(matrix3)
#stage1
f=open("stage2.txt",'r')
lines=f.read()
lines=lines.split()
#print(lines)
rhom=float(lines[0])
rho1=float(lines[1])
rho2=float(lines[2])
km=float(lines[3])
k1=float(lines[4])
k2=float(lines[5])
C=float(lines[6])
c1=float(lines[7])
c2=float(lines[8])
#n0=float(input("Enter the value of market share in 1st period:"))
n0=0.43
f.close()
matrix4=funMatrix(n0,choice)
#n_2=float(input("Enter the value of market share in 2nd period:"))
n_2=0.41

#Finding the Payoff Table for Stage 1
for i in range(0,4):
    if n_2==n2:
        matrix4[i]=list(map(add,matrix4[i],matrix2[i]))
    elif n_2==n1:
        matrix4[i]=list(map(add,matrix4[i],matrix1[i]))
    else:
        matrix4[i]=list(map(add,matrix4[i],matrix3[i]))

nash4=nashEqu(matrix4)
#print("The Nash Equilibrium of Stage1 lies at: ",nash4)
#print(matrix4)
l2=[]
for i in range(0,4):
    l2.append(matrix4[i][0]-matrix4[i][1])
ans=max(l2)
print(ans)
sol=l2.index(ans)
print(sol)
#print("The optimal solution will be obtained if option:",nash4[0]+1,nash4[1]+1," is selected in first period")
#print("The optimal solution will be obtained if option:",nash4+1," is selected in first period")


    