
from os.path import join, dirname
from yaml import load
from class_boid import boid 
c = load(open(join(dirname(__file__), 'config.yml')))

def update_boids(boids):
    
    for boid1 in boids: 
        for boid2 in boids:
             boid1.fly_towards_middle(boid2, c['Flying_inwards_factor'], c['boid_number'])
                         
             if boid1.distance(boid2) < c['Close_range']:
                boid1.fly_away_from_nearby(boid2)
                
    for boid1 in boids:
        for boid2 in boids:    
             if boid1.distance(boid2) < c['Long_range']:
                boid1.match_speed(boid2, c['Match_speed_factor'], c['boid_number'])
    for boid1, j in zip(boids, range(50)):
        boid1.x_position += boid1.x_velocity
        boid1.y_position += boid1.y_velocity
