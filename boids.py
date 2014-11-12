"""
An improved implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
using refactoring.
"""
from os.path import join, dirname
from matplotlib import pyplot as plt
from matplotlib import animation
import random
from yaml import load
from class_boid import boid 
from update_boids import update_boids 

# Note: This code would not work for me from command line, it would only work in Canopy
# However, this was also the case with the initial code given. 

config = load(open(join(dirname(__file__), 'config.yml')))


# The initial boids are randomly generated here. boids_x generates the x positions of the starting boids for example.

boids_x=[random.uniform(config['x_pos_min'],config['x_pos_max']) for x in range(config['boid_number'])]
boids_y=[random.uniform(config['y_pos_min'],config['y_pos_max']) for x in range(config['boid_number'])]
boid_x_velocities=[random.uniform(config['x_vel_min'],config['x_vel_max']) for x in range(config['boid_number'])]
boid_y_velocities=[random.uniform(config['y_vel_min'],config['y_vel_max']) for x in range(config['boid_number'])]

boids=[boid(boids_x[i],boids_y[i],boid_x_velocities[i], boid_y_velocities[i]) for i in range(config['boid_number'])]

update_boids(boids)    

x_plot = [boids[i].x_position for i in range(len(boids))]
y_plot = [boids[i].y_position for i in range(len(boids))]

figure=plt.figure()
axes=plt.axes(xlim=(config['xlim_min'],config['xlim_max']), ylim=(config['ylim_min'],config['xlim_max']))
scatter=axes.scatter(x_plot,y_plot)

def animate(frame):
   x_plot = [boids[i].x_position for i in range(len(boids))]
   y_plot = [boids[i].y_position for i in range(len(boids))]
   update_boids(boids)
   scatter.set_offsets(zip(x_plot,y_plot))


anim = animation.FuncAnimation(figure, animate,
                               frames=config['frames'], interval=config['frames'])

if __name__ == "__main__":
    plt.show()
