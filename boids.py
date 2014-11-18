"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random
from numpy import array

# Will now add an Eagle to Boids

class Boid(object):
    def __init__(self,x,y,xv,yv,owner):
        self.position=array([x,y])
        self.velocity=array([xv,yv])
        self.owner=owner
    def separation(self, other):
        separation=other.position-self.position   
        return separation

    def separation_sq(self, other):
        separation_sq=self.separation(other).dot(self.separation(other))
        return separation_sq
    def interaction(self, other):
        pass
        
class Eagle(Boid):
    def __init__(self,x,y,xv,yv,owner):
        super(Eagle, self).__init__(x,y,xv,yv,owner)
        
    def interaction(self,other):
        delta_v=array([0.0,0.0])
        delta_v+=self.separation(other)*self.owner.eagle_hunt_strength
        
        return delta_v

    def colour(self):
        return (1,0,0)
        
class Starling(Boid):
    def __init__(self,x,y,xv,yv,owner):
        super(Starling, self).__init__(x,y,xv,yv,owner)
        
    def interaction(self,other):
        delta_v=array([0.0,0.0])
        separation=other.position-self.position 
        if type(other)=="Eagle":
            # Flee the Eagle
            if self.separation_sq(other) < self.owner.eagle_avoidance_radius**2:
                delta_v-=(separation*self.owner.eagle_fear)/separation.dot(separation)
                return delta_v

        else:
            # Fly towards the middle
            delta_v+=separation*self.owner.flock_attraction
            
            # Fly away from nearby boids
            if self.separation_sq(other) < self.owner.avoidance_radius**2:
                delta_v-=separation

            # Try to match speed with nearby boids
            if self.separation_sq(other) < self.owner.formation_flying_radius**2:
                delta_v+=(other.velocity-self.velocity)*self.owner.speed_matching_strength

        return delta_v

    def colour(self):
        return (0,0,1)
        
# Deliberately terrible code for teaching purposes
class BoidsModel(object):
#    def initialise_random(self,count):
#        self.boids=[Starling(random.uniform(-450,50.0),
#                random.uniform(300.0,600.0),
#                random.uniform(0,10.0),
#                random.uniform(-20.0,20.0),self) for i in range(count)]
#
#
#    def add_eagle(self,x,y,xv,yv):
#        self.boids.append(Eagle(x,y,xv,yv,self))

    def update(self):
        for me in self.boids:
            delta_v=array([0.0,0.0])
            for him in self.boids:
                delta_v+=me.interaction(him)
            # Accelerate as stated
            me.velocity+=delta_v
            # Move according to velocities
            me.position+=me.velocity

class BoidsBuilder(object):
    def start_boids(self):
        self.boidsmodel = BoidsModel()
        
    def set_starling_properties(self, flock_attraction, avoidance_radius, 
    formation_flying_radius, speed_matching_strength):
        self.boidsmodel.flock_attraction=flock_attraction
        self.boidsmodel.avoidance_radius=avoidance_radius
        self.boidsmodel.formation_flying_radius=formation_flying_radius
        self.boidsmodel.speed_matching_strength=speed_matching_strength
            
    def set_eagle_properties(self, eagle_avoidance_radius, 
    eagle_fear, eagle_hunt_strength):
        self.boidsmodel.eagle_avoidance_radius = eagle_avoidance_radius
        self.boidsmodel.eagle_fear=eagle_fear
        self.boidsmodel.eagle_hunt_strength=eagle_hunt_strength
        
    def finish(self):
        return self.boidsmodel

        
class BoidsBuilderRandom(BoidsBuilder):
    def initialise(self,count):
        self.boidsmodel.boids = [Starling(random.uniform(-450,50.0),
                random.uniform(300.0,600.0),
                random.uniform(0,10.0),
                random.uniform(-20.0,20.0), self.boidsmodel) for i in range(count)]
    def add_eagle(self,x,y,xv,yv):
        self.boidsmodel.boids.append(Eagle(x,y,xv,yv,self.boidsmodel))


                
class BoidsBuilderData(BoidsBuilder):
    def initialise(self,data):
        self.boidsmodel.boids=[Starling(x,y,xv,yv,self.boidsmodel) for x,y,xv,yv in zip(*data)]

        
