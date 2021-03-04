import numpy as np 
import matplotlib.pyplot as plt 

dimension=40
steps=40
X=np.linspace(-dimension,dimension,steps)
Y=np.linspace(-dimension,dimension,steps)

Xo=0                # Obstacle x coordinate 
Yo=0                # Obstacle y coordinate
r=2                 # Obstacle radius
s=15                # Obstacle s value
beta=3              # Scaling factor


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
        theta=np.arctan2((Yo-y),(Xo-x))
        color.append(theta)
        d=np.sqrt( (Xo-x)**2 + (Yo-y)**2 )
        if d< r:
            dx=float('inf')
            dy=float('inf')
        elif d>s+r:
            dx=0
            dy=0
        else:
            dx=-beta*(s+r-d)*np.cos(theta)
            dy=-beta*(s+r-d)*np.sin(theta)
        dx_.append(dx)
        dy_.append(dy)
        # color.append(dy)

fig, ax=plt.subplots(figsize=(14,9))
ax.quiver(x_,y_,dx_,dy_,scale_units ='xy', scale = 20)#,alpha=1,headwidth=1,headlength=2,headaxislength=10)
# plt.set_aspect('equal')

obstacle_circle=plt.Circle((Xo,Yo),r,color='red')
ax.add_patch(obstacle_circle)
ax.set_aspect('equal')
plt.show()