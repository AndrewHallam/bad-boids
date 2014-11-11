from boids import update_boids
from nose.tools import assert_almost_equal
import os
import yaml
from class_boid import boid 

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    data_before=regression_data["before"]
    boids_before=[boid(data_before[i]['x_position'],data_before[i]['y_position'],data_before[i]['x_velocity'],data_before[i]['y_velocity']) for i in range(50)]
    update_boids(boids_before)
    
    data_after=regression_data["after"]
    boids_after=[boid(data_after[i]['x_position'],data_after[i]['y_position'],data_after[i]['x_velocity'],data_after[i]['y_velocity']) for i in range(50)]

    for after,before in zip(boids_after,boids_before):
        assert_almost_equal(after.x_position,before.x_position,delta=100)
	
