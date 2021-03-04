import numpy as np 
import matplotlib.pyplot as plt 
import random as rnd 

Xs=-60                # Robot start point
Ys=-80                # Robot start point

dimension=80
no=70
X=np.linspace(-dimension,dimension,no)
Y=np.linspace(-dimension,dimension,no)


# Goal Data
Xg=20                # Goal x coordinate 
Yg=25                # Goal y coordinate
rg=2                 # Goal radius
sg=15                # Goal s value
alpha=3             # Scaling factor

                
N=10                        #Number of obstacles
Xo=[]                       # Obstacle x coordinate array
Yo=[]                       # Obstacle y coordinate array
ro=[]                       # Obstacle radius array
for i in range(0,N):
    flag=True
    x=0
    y=0
    r=0
    while(flag):
        x=rnd.randrange(-75,75)
        y=rnd.randrange(-75,75)
        r=rnd.randrange(1,5)
        dist=np.sqrt( (Xg-x)**2 + (Yg-y)**2 )
        if (dist>r+rg+20):
            flag=False
    Xo.append(x)
    Yo.append(y)
    ro.append(r)
# Xo=[2.5,-39,0,-9,-44,14,35,-44,-17,-69]
# Yo=[-1.07,-45,-30,4,-75,-43,-7,-11,-34,-51]
# ro=[1,2,1,2,2,3,4,1,3,2]
so=20                # Obstacle s value
beta=4              # Scaling factor



def attractionPotential(x,y):
    theta_g=np.arctan2((Yg-y),(Xg-x))
    # color.append(theta)
    dg=np.sqrt( (Xg-x)**2 + (Yg-y)**2 )
    if dg< rg:
        dxg=0
        dyg=0
    elif dg>sg+ rg:
        dxg=alpha*sg*np.cos(theta_g)
        dyg=alpha*sg*np.sin(theta_g)
    else:
        dxg=alpha*(dg-rg)*np.cos(theta_g)
        dyg=alpha*(dg-rg)*np.sin(theta_g)
    return dxg,dyg

def repulsionPotential(x,y):
    count=0
    dxo_=0
    dyo_=0
    for i in range(0,N):
        xo=Xo[count]
        yo=Yo[count]
        theta_o=np.arctan2((yo-y),(xo-x))
        do=np.sqrt( (xo-x)**2 + (yo-y)**2 )
        if do< ro[count]:
            dxo=float('inf')
            dyo=float('inf')
        elif do>so+ro[count]:
            dxo=0
            dyo=0
        else:
            dxo=-beta*(so+ro[count]-do)*np.cos(theta_o)
            dyo=-beta*(so+ro[count]-do)*np.sin(theta_o)
        count+=1
        dxo_+=dxo
        dyo_+=dyo
    return dxo_,dyo_

x_=[]
dx_=[]
y_=[]
dy_=[]

colors=[]
for x in X:
    for y in Y:
        x_.append(x)
        y_.append(y)
        dxg,dyg=attractionPotential(x,y)
        dxo,dyo=repulsionPotential(x,y)
        dx_.append(dxo+dxg)
        dy_.append(dyo+dyg)

path_x=[]
path_y=[]
path_dx=[]
path_dy=[]



steps=abs(X[0]-X[1])*3
count_1=0
while( not (round(np.sqrt( (Xs-Xg)**2 + (Ys-Yg)**2 ) ,2)<=rg)):
    path_x.append(Xs)
    path_y.append(Ys)
    dxg,dyg=attractionPotential(Xs,Ys)


    dxo,dyo=repulsionPotential(Xs,Ys)
    
    
    # print("({},{}),".format(Xs,Ys))
    Xs=Xs+(dxo/steps)+(dxg/steps)
    Ys=Ys+(dyo/steps)+(dyg/steps)
    # print("({},{})\n".format(Xs,Ys))
    path_dx.append((dxo/steps)+(dxg/steps))
    path_dy.append((dyo/steps)+(dyg/steps))
    count_1+=1
    if count_1>2000:
        print("Something wrong with the generation of obstacles....re-run the code!!\n")
        break
# print(path_dx)


fig, ax=plt.subplots(figsize=(14,9))
ax.quiver(x_,y_,dx_,dy_,scale_units ='xy', scale = 20)#,alpha=1,headwidth=1,headlength=2,headaxislength=10)
# ax.quiver(path_x,path_y,path_dx,path_dy,0.1235,scale_units ='xy', scale = 20)
ax.plot(path_x,path_y,color='orange')
goal_circle=plt.Circle((Xg,Yg),rg,color='blue')
# obstacle_circle=plt.Circle((Xo,Yo),ro,color='red')
ax.add_patch(goal_circle)
print("Obstacle Coordinates:\n")
for i in range(0,N):
    print("({},{})|radius:{}".format(Xo[i],Yo[i],ro[i]))
    obstacle_circle=plt.Circle((Xo[i],Yo[i]),ro[i],color='red')
    ax.add_patch(obstacle_circle)
# ax.add_patch(obstacle_circle)
ax.set_aspect('equal')
plt.show()

# print("Obstacle Coordinates:\n")
# for i in range(0,N):
#     print("({},{})|radius:{}".format(Xo[i],Yo[i],ro[i]))