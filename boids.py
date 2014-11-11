"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""
from os.path import join, dirname
from matplotlib import pyplot as plt
from matplotlib import animation
import random
from yaml import load
from class_boid import boid 
# Deliberately terrible code for teaching purposes

c = load(open(join(dirname(__file__), 'config.yml')))

boids_x=[random.uniform(c['x_pos_min'],c['x_pos_max']) for x in range(c['boid_number'])]
boids_y=[random.uniform(c['y_pos_min'],c['y_pos_max']) for x in range(c['boid_number'])]
boid_x_velocities=[random.uniform(c['x_vel_min'],c['x_vel_max']) for x in range(c['boid_number'])]
boid_y_velocities=[random.uniform(c['y_vel_min'],c['y_vel_max']) for x in range(c['boid_number'])]

boids=[boid(boids_x[i],boids_y[i],boid_x_velocities[i], boid_y_velocities[i]) for i in range(c['boid_number'])]

def update_boids(boids):
    
    for boid1 in boids:
        for boid2 in boids:
            boid1.fly_towards_middle(boid2, c['Flying_inwards_factor'], c['boid_number'])
            
            if boid1.distance(boid2) < c['Close_range']:
               boid1.fly_away_from_nearby(boid2)
               
            if boid1.distance(boid2) < c['Long_range']:
               boid1.match_speed(boid2, c['Match_speed_factor'], c['boid_number'])
            
        boid1.x_position = boid1.x_position + boid1.x_velocity
        boid1.y_position = boid1.y_position + boid1.y_velocity

x_plot = [boids[i].x_position for i in range(len(boids))]
y_plot = [boids[i].y_position for i in range(len(boids))]

figure=plt.figure()
axes=plt.axes(xlim=(c['xlim_min'],c['xlim_max']), ylim=(c['ylim_min'],c['xlim_max']))
scatter=axes.scatter(x_plot,y_plot)

def animate(frame):
   x_plot = [boids[i].x_position for i in range(len(boids))]
   y_plot = [boids[i].y_position for i in range(len(boids))]
   update_boids(boids)
   scatter.set_offsets(zip(x_plot,y_plot))


anim = animation.FuncAnimation(figure, animate,
                               frames=c['frames'], interval=c['frames'])

if __name__ == "__main__":
    plt.show()
