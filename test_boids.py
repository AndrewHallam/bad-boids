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

test_bad_boids_regression()