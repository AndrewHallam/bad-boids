
from os.path import join, dirname
from yaml import load
from class_boid import boid 
config = load(open(join(dirname(__file__), 'config.yml')))

# update_boids will change the position and velocity of each of the boids by considering the other boids.

def update_boids(boids):
    
    for boid1 in boids: 
        for boid2 in boids:
            
             boid1.fly_towards_middle(boid2, config['Flying_inwards_factor'], config['boid_number'])
                        
             if boid1.distance(boid2) < config['Close_range']:
                boid1.fly_away_from_nearby(boid2)
                
# Match speed has been put in it's own for loops so the "other boids" velocities are used to update
# each individual boids velocity is consistent with the code given.                
    for boid1 in boids:
        for boid2 in boids:    
            
             if boid1.distance(boid2) < config['Long_range']:
                boid1.match_speed(boid2, config['Match_speed_factor'], config['boid_number'])
                
    for boid1, j in zip(boids, range(50)):
        boid1.x_position += boid1.x_velocity
        boid1.y_position += boid1.y_velocity
