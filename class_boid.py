class boid(object):
   def __init__(self, x_position, y_position, x_velocity, y_velocity):
       self.x_position=x_position
       self.y_position=y_position
       self.x_velocity=x_velocity
       self.y_velocity=y_velocity

   def fly_towards_middle(self, other_boid, weight):
      self.x_velocity += (other_boid.x_position-self.x_position)*weight
      self.y_velocity += (other_boid.y_position-self.y_position)*weight
     


