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

def fly_towards_middle(velocity, position, boid1, boid2, weighting_factor, boidnumber):
   velocity[boid1] += (position[boid2]-position[boid1])*weighting_factor/boidnumber
   
def distance(x_position, y_position,  boid1, boid2):
   return (x_position[boid2]-x_position[boid1])**2 + (y_position[boid2]-y_position[boid1])**2

def fly_away_from_nearby(x_position, y_position, x_velocity, y_velocity, boid1, boid2, nearby_factor):
   if distance(x_position, y_position,  boid1, boid2) < nearby_factor:
				x_velocity[boid1]=x_velocity[boid1]+(x_position[boid1]-x_position[boid2])
				y_velocity[boid1]=y_velocity[boid1]+(y_position[boid1]-y_position[boid2])

def match_speed(x_position, y_position, x_velocity, y_velocity, boid1, boid2, far_factor, speed_factor, boidnumber):
   if distance(x_position, y_position,  boid1, boid2) < far_factor:
	x_velocity[boid1]=x_velocity[boid1]+(x_velocity[boid2]-x_velocity[boid1])*speed_factor/boidnumber
        y_velocity[boid1]=y_velocity[boid1]+(y_velocity[boid2]-y_velocity[boid1])*speed_factor/boidnumber

def update_boids(boids):
	x_pos,y_pos,x_vel,y_vel=boids
	# Fly towards the middle
	for i in range(c['boid_number']):
	   for j in range(c['boid_number']):
	      fly_towards_middle(x_vel, x_pos, i, j, c['Flying_inwards_factor'], c['boid_number'])
	      
	for i in range(c['boid_number']):
	   for j in range(c['boid_number']):
	      fly_towards_middle(y_vel, y_pos, i, j, c['Flying_inwards_factor'], c['boid_number'])
	      
	# Fly away from nearby boids
	for i in range(c['boid_number']):
	   for j in range(c['boid_number']):
	      fly_away_from_nearby(x_pos, y_pos, x_vel, y_vel, i, j,  c['Close_range'])
	      
	# Try to match speed with nearby boids
	for i in range(c['boid_number']):
	   for j in range(c['boid_number']):
	      match_speed(x_pos, y_pos, x_vel, y_vel, i, j, c['Long_range'], c['Match_speed_factor'], c['boid_number'])
	      
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
