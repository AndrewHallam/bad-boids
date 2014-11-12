from update_boids import update_boids
from nose.tools import assert_almost_equal
import os
import yaml
from class_boid import boid 

def test_bad_boids_regression():
# This tests that the upgrade_boids() function is properly updating the positions and momentums
# of each boid in an individual time step.     

# This section loads the initial data and runs it through a single ugrade_boids()        
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    data_before=regression_data["before"]
    boids_before=[boid(data_before[0][i],data_before[1][i],data_before[2][i],data_before[3][i]) for i in range(50)]
    update_boids(boids_before)

# This section loads the final data which can then be compared to the initial data put through
# the function  
    data_after=regression_data["after"]
    boids_after=[boid(data_after[0][i],data_after[1][i],data_after[2][i],data_after[3][i]) for i in range(50)]

    for after,before in zip(boids_after,boids_before):
        assert_almost_equal(after.x_position,before.x_position,delta=0.01)
        assert_almost_equal(after.y_position,before.y_position,delta=0.01)
        assert_almost_equal(after.x_velocity,before.x_velocity,delta=0.01)
        assert_almost_equal(after.y_velocity,before.y_velocity,delta=0.01)

def test_fly_towards_middle():
# This test checks fly_towards_middle() properly updates velocities.
        
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fly_towards_middle.yml')))
    data_before=regression_data["before"]
    boids_before=[boid(data_before[0][i],data_before[1][i],data_before[2][i],data_before[3][i]) for i in range(2)]
    
# Two boids are defined but fly_towards_middle() is only used on one
    boids_before[0].fly_towards_middle(boids_before[1], 1., 2.)

    data_after=regression_data["after"]
    boids_after=[boid(data_after[0][i],data_after[1][i],data_after[2][i],data_after[3][i]) for i in range(2)]

# Even though only one boid had the function applied to it we also check the second
# boid didn't get changed by accident. 
    for after,before in zip(boids_after,boids_before):
        assert_almost_equal(after.x_position,before.x_position,delta=0.01)
        assert_almost_equal(after.y_position,before.y_position,delta=0.01)
        assert_almost_equal(after.x_velocity,before.x_velocity,delta=0.01)
        assert_almost_equal(after.y_velocity,before.y_velocity,delta=0.01)

def  test_distance():
# We check the distance() method between two boids is correct for two boids. 
# Note once again that we are finding the distance squared. 
    
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'sample_distance.yml')))
    data=regression_data["boids"]
    boids=[boid(data[0][i],data[1][i],data[2][i],data[3][i]) for i in range(2)]
    assert_almost_equal(boids[0].distance(boids[1]), 200., delta=0.01)
    
def test_fly_away_from_nearby():
# We check the fly_away_from_nearby() method works properly for two boids. 
        
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'sample_fly_away_from_nearby.yml')))
    data=regression_data["before"]
    boids_before=[boid(data[0][i],data[1][i],data[2][i],data[3][i]) for i in range(2)]

# Once again, only the first boid has been effected but both boids are checked.         
    boids_before[0].fly_away_from_nearby(boids_before[1])

    data_after=regression_data["after"]
    boids_after=[boid(data_after[0][i],data_after[1][i],data_after[2][i],data_after[3][i]) for i in range(2)]
       
    for after, before in zip(boids_after,boids_before):
        assert_almost_equal(after.x_position,before.x_position,delta=0.01)
        assert_almost_equal(after.y_position,before.y_position,delta=0.01)
        assert_almost_equal(after.x_velocity,before.x_velocity,delta=0.01)
        assert_almost_equal(after.y_velocity,before.y_velocity,delta=0.01)

def test_match_speed():
# We check the match_speed() method works properly for two boids.     
    
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'sample_match_speed.yml')))
    data=regression_data["before"]
    boids_before=[boid(data[0][i],data[1][i],data[2][i],data[3][i]) for i in range(2)]
    boids_before[0].match_speed(boids_before[1], 1., 2.)

    data_after=regression_data["after"]
    boids_after=[boid(data_after[0][i],data_after[1][i],data_after[2][i],data_after[3][i]) for i in range(2)]
    
    for after, before in zip(boids_after,boids_before):
        assert_almost_equal(after.x_position,before.x_position,delta=0.01)
        assert_almost_equal(after.y_position,before.y_position,delta=0.01)
        assert_almost_equal(after.x_velocity,before.x_velocity,delta=0.01)
        assert_almost_equal(after.y_velocity,before.y_velocity,delta=0.01)
