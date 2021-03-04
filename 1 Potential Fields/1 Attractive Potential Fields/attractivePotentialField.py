import numpy as np 
import matplotlib.pyplot as plt 

dimension=40
steps=40
X=np.linspace(-dimension,dimension,steps)
Y=np.linspace(-dimension,dimension,steps)

Xg=0                # Goal x coordinate 
Yg=0                # Goal y coordinate
r=2                 # Goal radius
s=15                # Goal s value
alpha=3             # Scaling factor


x_=[]
dx_=[]
y_=[]
dy_=[]
color=[]
widths = np.linspace(0, 2, X.size)
#Computing the Potential Functions
for x in X:
    for y in Y:
        x_.append(x)
        y_.append(y)
        theta=np.arctan2((Yg-y),(Xg-x))
        color.append(theta)
        d=np.sqrt( (Xg-x)**2 + (Yg-y)**2 )
        if d< r:
            dx=0
            dy=0
        elif d>s+ r:
            dx=alpha*s*np.cos(theta)
            dy=alpha*s*np.sin(theta)
        else:
            dx=alpha*(d-r)*np.cos(theta)
            dy=alpha*(d-r)*np.sin(theta)
        dx_.append(dx)
        dy_.append(dy)

fig, ax=plt.subplots(figsize=(9,9))
ax.quiver(x_,y_,dx_,dy_,scale_units ='xy', scale = 20)
goal_circle=plt.Circle((Xg,Yg),r,color='blue')
ax.add_patch(goal_circle)
ax.set_aspect('equal')
plt.show()