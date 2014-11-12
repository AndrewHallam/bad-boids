# This defines each of the "boid"s flying around in the animation.

class boid(object):
   def __init__(self, x_position, y_position, x_velocity, y_velocity):
       self.x_position=x_position
       self.y_position=y_position
       self.x_velocity=x_velocity
       self.y_velocity=y_velocity

   def fly_towards_middle(self, other_boid, weight, boid_number):
      self.x_velocity += (other_boid.x_position-self.x_position)*weight/boid_number
      self.y_velocity += (other_boid.y_position-self.y_position)*weight/boid_number
     
   # Distance actually finds the distance squared, although this is not an issue for it's use in this code.   
   def distance(self, other_boid):
      return (other_boid.x_position-self.x_position)**2 + (other_boid.y_position-self.y_position)**2
      
   def fly_away_from_nearby(self, other_boid):
         self.x_velocity += self.x_position - other_boid.x_position
         self.y_velocity += self.y_position - other_boid.y_position

   def match_speed(self, other_boid, weight, boid_number):
        self.x_velocity += (other_boid.x_velocity - self.x_velocity)*weight/boid_number
        self.y_velocity += (other_boid.y_velocity - self.y_velocity)*weight/boid_number
