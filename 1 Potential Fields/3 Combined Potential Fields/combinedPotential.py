import numpy as np 
import matplotlib.pyplot as plt 

dimension=80
steps=70
X=np.linspace(-dimension,dimension,steps)
Y=np.linspace(-dimension,dimension,steps)

# Obstacle Data
Xo=-20                # Obstacle x coordinate 
Yo=-25                # Obstacle y coordinate
ro=2                 # Obstacle radius
so=20                # Obstacle s value
beta=4              # Scaling factor

# Goal Data
Xg=20                # Goal x coordinate 
Yg=25                # Goal y coordinate
rg=2                 # Goal radius
sg=15                # Goal s value
alpha=3             # Scaling factor


x_=[]
dx_=[]
y_=[]
dy_=[]
color=[]
widths = np.linspace(0, 2, X.size)
for x in X:
    for y in Y:
        x_.append(x)
        y_.append(y)
        theta_o=np.arctan2((Yo-y),(Xo-x))
        # color.append(theta_o)
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
        dx_.append(dxo+dxg)
        dy_.append(dyo+dyg)

        color.append((theta_g+theta_o)/2)

# print("x:{},y:{},dx_:{},dy_:{}".format(len(x_),len(y_),len(dx_),len(dy_)))

fig, ax=plt.subplots(figsize=(14,9))
ax.quiver(x_,y_,dx_,dy_,scale_units ='xy', scale = 20)#,alpha=1,headwidth=1,headlength=2,headaxislength=10)
# plt.set_aspect('equal').
goal_circle=plt.Circle((Xg,Yg),rg,color='blue')
obstacle_circle=plt.Circle((Xo,Yo),ro,color='red')
ax.add_patch(goal_circle)
ax.add_patch(obstacle_circle)
ax.set_aspect('equal')
plt.show()