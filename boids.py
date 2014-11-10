"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""
from os.path import join, dirname
from matplotlib import pyplot as plt
from matplotlib import animation
import random
from yaml import load
# Deliberately terrible code for teaching purposes

c = load(open(join(dirname(__file__), 'config.yml')))

boids_x=[random.uniform(c['x_pos_min'],c['x_pos_max']) for x in range(c['boid_number'])]
boids_y=[random.uniform(c['y_pos_min'],c['y_pos_max']) for x in range(c['boid_number'])]
boid_x_velocities=[random.uniform(c['x_vel_min'],c['x_vel_max']) for x in range(c['boid_number'])]
boid_y_velocities=[random.uniform(c['y_vel_min'],c['y_vel_max']) for x in range(c['boid_number'])]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
	x_pos,y_pos,x_vel,y_vel=boids
	# Fly towards the middle
	for i in range(len(x_pos)):
		for j in range(len(x_pos)):
			x_vel[i]=x_vel[i]+(x_pos[j]-x_pos[i])*c['Flying_inwards_factor']/len(x_pos)
	for i in range(len(x_pos)):
		for j in range(len(x_pos)):
			y_vel[i]=y_vel[i]+(y_pos[j]-y_pos[i])*c['Flying_inwards_factor']/len(x_pos)
	# Fly away from nearby boids
	for i in range(len(x_pos)):
		for j in range(len(x_pos)):
			if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < c['Close_range']:
				x_vel[i]=x_vel[i]+(x_pos[i]-x_pos[j])
				y_vel[i]=y_vel[i]+(y_pos[i]-y_pos[j])
	# Try to match speed with nearby boids
	for i in range(len(x_pos)):
		for j in range(len(x_pos)):
			if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < c['Long_range']:
				x_vel[i]=x_vel[i]+(x_vel[j]-x_vel[i])*c['Match_speed_factor']/len(x_pos)
				y_vel[i]=y_vel[i]+(y_vel[j]-y_vel[i])*c['Match_speed_factor']/len(x_pos)
	# Move according to velocities
	for i in range(len(x_pos)):
		x_pos[i]=x_pos[i]+x_vel[i]
		y_pos[i]=y_pos[i]+y_vel[i]


figure=plt.figure()
axes=plt.axes(xlim=(c['xlim_min'],c['xlim_max']), ylim=(c['ylim_min'],c['xlim_max']))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=c['frames'], interval=c['frames'])

if __name__ == "__main__":
    plt.show()
