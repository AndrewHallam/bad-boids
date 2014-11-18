from boids import BoidsModel, BoidsBuilderRandom
from matplotlib import pyplot as plt
from matplotlib import animation

builder=BoidsBuilderRandom()
builder.start_boids()
builder.set_starling_properties(0.01/50, 10, 100, 0.125/50)
builder.set_eagle_properties(100, 5000, 0.00005)
builder.initialise(50)
builder.add_eagle(0,0,0,50)
boidsmodel=builder.finish()

#
figure=plt.figure()
axes=plt.axes(xlim=(-2000,1500), ylim=(-500,4000))
scatter=axes.scatter([b.position[0] for b in boidsmodel.boids],[b.position[1] for b in boidsmodel.boids])


def color(boid):
	if type(boid)=="Eagle":
		return (1,0,0)
	return (0,0,1)

def animate(frame):
    boidsmodel.update()
    scatter.set_offsets([b.position for b in boidsmodel.boids])
    scatter.set_color([b.colour() for b in boidsmodel.boids])



anim = animation.FuncAnimation(figure, animate,
        frames=50, interval=50)

if __name__ == "__main__":
    plt.show()

#from boids import Boids, BoidsBuilderRandom
#from matplotlib import pyplot as plt
#from matplotlib import animation
#
#builder=BoidsBuilderRandom()
#builder.start_boids()
#builder.set_starling_properties(0.01/50, 10, 100, 0.125/50)
#builder.set_eagle_properties(100, 5000, 0.00005)
#builder.initialise_random(50)
#builder.add_eagle(0,0,0,50)
#boids=builder.finish()

#from boids import Boids, BoidsBuilder
#from matplotlib import pyplot as plt
#from matplotlib import animation
#
#builder=BoidsBuilder()
#builder.start_boids()
#builder.set_starling_properties(0.01/50, 10, 100, 0.125/50)
#builder.set_eagle_properties(100, 5000, 0.00005)
#boids=builder.finish()
#boids.initialise_random(50)
#boids.add_eagle(0,0,0,50)
#
