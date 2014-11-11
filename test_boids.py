from update_boids import update_boids
from nose.tools import assert_almost_equal
import os
import yaml
from class_boid import boid 

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    data_before=regression_data["before"]
    boids_before=[boid(data_before[0][i],data_before[1][i],data_before[2][i],data_before[3][i]) for i in range(50)]
    update_boids(boids_before)
  
    data_after=regression_data["after"]
    boids_after=[boid(data_after[0][i],data_after[1][i],data_after[2][i],data_after[3][i]) for i in range(50)]

    for after,before in zip(boids_after,boids_before):
        assert_almost_equal(after.x_position,before.x_position,delta=0.01)
        assert_almost_equal(after.y_position,before.y_position,delta=0.01)
        assert_almost_equal(after.x_velocity,before.x_velocity,delta=0.01)
        assert_almost_equal(after.y_velocity,before.y_velocity,delta=0.01)

def test_fly_towards_middle():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fly_towards_middle.yml')))
    data_before=regression_data["before"]
    boids_before=[boid(data_before[0][i],data_before[1][i],data_before[2][i],data_before[3][i]) for i in range(2)]
    boids_before[0].fly_towards_middle(boids_before[1], 1, 1)
    print '{},{},{},{}'.format(boids_before[0].x_position, boids_before[0].y_position, boids_before[0].x_velocity, boids_before[0].y_velocity)
    boids_after=[boid(0, 0, 1, 1), boid(1, 1, 0, 0)]
    
    for after,before in zip(boids_after,boids_before):
        assert_almost_equal(after.x_position,before.x_position,delta=0.01)
        assert_almost_equal(after.y_position,before.y_position,delta=0.01)
        assert_almost_equal(after.x_velocity,before.x_velocity,delta=0.01)
        assert_almost_equal(after.y_velocity,before.y_velocity,delta=0.01)

def 