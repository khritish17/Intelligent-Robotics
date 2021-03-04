import numpy as np 
import matplotlib.pyplot as plt 

Xs=-60                # Robot start point
Ys=-80                # Robot start point

dimension=80
no=70
X=np.linspace(-dimension,dimension,no)
Y=np.linspace(-dimension,dimension,no)

# Obstacle Data
Xo=-20                # Obstacle x coordinate 
Yo=-25                # Obstacle y coordinate
ro=7                 # Obstacle radius
so=20                # Obstacle s value
beta=4              # Scaling factor
obstacle_x=[]
obstacle_y=[]

# Goal Data
Xg=20                # Goal x coordinate 
Yg=25                # Goal y coordinate
rg=2                 # Goal radius
sg=15                # Goal s value
alpha=3             # Scaling factor
goal_x=[]
goal_y=[]

def attractionPotential(x,y):
    theta_g=np.arctan2((Yg-y),(Xg-x))
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
    theta_o=np.arctan2((Yo-y),(Xo-x))
    do=np.sqrt( (Xo-x)**2 + (Yo-y)**2 )
    if do< ro:
        dxo=float('inf')
        dyo=float('inf')
    elif do>so+ro:
        dxo=0
        dyo=0
    else:
        dxo=-beta*(so+ro-do)*np.cos(theta_o)
        dyo=-beta*(so+ro-do)*np.sin(theta_o)
    return dxo,dyo

x_=[]
dx_=[]
y_=[]
dy_=[]

colors=[]
for x in X:
    for y in Y:
        x_.append(x)
        y_.append(y)
        dxo,dyo=repulsionPotential(x,y)
        dxg,dyg=attractionPotential(x,y)
        colors.append(np.arctan2(dxo+dxg,dyo+dyg))
        dx_.append(dxo+dxg)
        dy_.append(dyo+dyg)

path_x=[]
path_y=[]
path_dx=[]
path_dy=[]


count=0
steps=abs(X[0]-X[1])*5


while( not (round(np.sqrt( (Xs-Xg)**2 + (Ys-Yg)**2 ) ,3)<=rg)):
    path_x.append(Xs)
    path_y.append(Ys)
    dxo,dyo=repulsionPotential(Xs,Ys)
    dxg,dyg=attractionPotential(Xs,Ys)
    
    
    Xs=Xs+(dxo/steps)+(dxg/steps)
    Ys=Ys+(dyo/steps)+(dyg/steps)
    
    path_dx.append((dxo/steps)+(dxg/steps))
    path_dy.append((dyo/steps)+(dyg/steps))
    


fig, ax=plt.subplots(figsize=(14,9))
ax.quiver(x_,y_,dx_,dy_,scale_units ='xy', scale = 20)
ax.plot(path_x,path_y,color='orange')
goal_circle=plt.Circle((Xg,Yg),rg,color='blue')
obstacle_circle=plt.Circle((Xo,Yo),ro,color='red')
ax.add_patch(goal_circle)
ax.add_patch(obstacle_circle)
ax.set_aspect('equal')
plt.show()
