"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

boid_number=50
x_pos_range=(-450,50.0)
y_pos_range=(300.0,600.0)
x_vel_range=(0,10.0)
y_vel_range=(-20.0,20.0) 

xlim=(-500,1500)
ylim=(-500,1500)

boids_x=[random.uniform(*x_pos_range) for x in range(boid_number)]
boids_y=[random.uniform(*y_pos_range) for x in range(boid_number)]
boid_x_velocities=[random.uniform(*x_vel_range) for x in range(boid_number)]
boid_y_velocities=[random.uniform(*y_vel_range) for x in range(boid_number)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
	x_pos,y_pos,x_vel,y_vel=boids
	# Fly towards the middle
	for i in range(len(x_pos)):
		for j in range(len(x_pos)):
			x_vel[i]=x_vel[i]+(x_pos[j]-x_pos[i])*0.01/len(x_pos)
	for i in range(len(x_pos)):
		for j in range(len(x_pos)):
			y_vel[i]=y_vel[i]+(y_pos[j]-y_pos[i])*0.01/len(x_pos)
	# Fly away from nearby boids
	for i in range(len(x_pos)):
		for j in range(len(x_pos)):
			if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < 100:
				x_vel[i]=x_vel[i]+(x_pos[i]-x_pos[j])
				y_vel[i]=y_vel[i]+(y_pos[i]-y_pos[j])
	# Try to match speed with nearby boids
	for i in range(len(x_pos)):
		for j in range(len(x_pos)):
			if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < 10000:
				x_vel[i]=x_vel[i]+(x_vel[j]-x_vel[i])*0.125/len(x_pos)
				y_vel[i]=y_vel[i]+(y_vel[j]-y_vel[i])*0.125/len(x_pos)
	# Move according to velocities
	for i in range(len(x_pos)):
		x_pos[i]=x_pos[i]+x_vel[i]
		y_pos[i]=y_pos[i]+y_vel[i]


figure=plt.figure()
axes=plt.axes(xlim=xlim, ylim=ylim)
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
