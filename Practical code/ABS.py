from matplotlib import pyplot as plt
import numpy as np

w0 = 200
v0 = 50
Tb = 600
M0 = 4220.2

Ts=0.05
Iw=2.12
rd=0.25

uh=0.8
ug=0.6

s0=0.2
m=300
g=9.8

w=[]
v=[]
t=[]
s=[]
w.append(200)
v.append(50)
s.append(0)
t.append(0)
k=0
i=0

while v0>0:
    k=k+1
    sb=(v0-rd*w0)/v0 #滑移率sb的定义，用速度和角速度计算滑移率
    s.append(sb)#用s保留当前滑移率
    #计算附着系数
    
    if sb<=s0:
        u=uh/s0*sb#前半部分的滑移率
    else:
        u=uh-(uh-ug)*(sb-s0)/(1-s0)
        #u=(uh-ug*s0)/(1-s0)-rd*sb;
    
    Fxb=u*m*g
    #计算制动力矩
    if sb>0.22:
        Tb=Tb-M0*Ts
    else: 
        if sb<0.18:
            Tb=Tb+M0*Ts
        else:
            Tb=Tb
    
    w0=w0+(Fxb*rd-Tb)/Iw*Ts#计算新的角速度和速度再带入前面
    w.append(w0)
    v0=v0-Fxb/m*Ts
    v.append(v0)
    i=i+1
    t.append(Ts*k)
    



#t=[0:Ts:Ts*k];
plt.plot(t,w, color ='red', linewidth = 1.0, linestyle ='-',label='角速度变化曲线')
#t=[0:Ts:Ts*k];
plt.show()
