import matplotlib.pyplot as plt
from numpy import array, average, c_
from matplotlib.animation import FuncAnimation


def make_animation(particlesX, particlesY, truePosX, truePosY, weights = None, background_image = None, aspect_ratio = None, filename = None):
    print("animation started")
    #------------------
    # Some basic set-up
    #------------------
    if isinstance(aspect_ratio, type(None)): # checking what the aspect ratio is
        fig, ax = plt.subplots(figsize=(5, 3)) # setting up figue and its aspect ratio
    else: # if ratio provided, we set it as that
        fig, ax = plt.subplots(figsize=aspect_ratio) # setting up figue and its aspect ratio
    
    ax.set(xlim=(0, background_image.shape[1]), ylim=(0, background_image.shape[0])) # set-up of plot limits based on background

    # I'm shortening the array names here, for my own convenience
    # Fetching particles, just in case, a bit unnecessary
    animPx = array(particlesX)
    animPy = array(particlesY)

    # True location
    #--------------
    truePx = truePosX
    truePy = truePosY

    # Location guess
    #---------------

    if weights is None:
        xguess = average(animPx[0,:], axis=None, returned=False)
        yguess = average(animPy[0,:], axis=None, returned=False)
    else:
        xguess = average(animPx[0,:], axis=None, weights=weights[0], returned=False)
        yguess = average(animPy[0,:], axis=None, weights=weights[0], returned=False)

    #-----------------
    # Initial plotting
    #-----------------
    # - Particles      - blue
    # - Location true  - cyan
    # - Location guess - red

    if not isinstance(background_image, type(None)):
        ax.imshow(background_image, cmap='gist_earth') # plotting the background image
    
    scat_particles = ax.scatter(animPx[0,:], animPy[0,:], color = 'purple', label = 'particles')
    scat_true = ax.scatter(truePx[0], truePy[0], color ="cyan", label = 'true location')
    scat_guess = ax.scatter(xguess, yguess, color="red", label = 'estimated location')
    ax.legend()
    
    #-----------------------
    # Updating scatter-plots
    #-----------------------
    def animate(i):
        # Particles - Update
        scat_particles.set_offsets(c_[animPx[i,:],animPy[i,:]])

        # Guess - Update
        if weights is None:
            xguess = average(animPx[i,:], axis=None, returned=False)
            yguess = average(animPy[i,:], axis=None, returned=False)
        else:
            xguess = average(animPx[i,:], axis=None, weights=weights[i], returned=False)
            yguess = average(animPy[i,:], axis=None, weights=weights[i], returned=False)

        scat_guess.set_offsets(c_[xguess, yguess])

        # True Location - Update
        scat_true.set_offsets(c_[truePx[i],truePy[i]])

    # Biggest fun
    anim = FuncAnimation(
        fig, animate, interval=100, frames=len(truePx)-1)
    
    # Drawing 
    plt.draw()
    plt.show()

    print("saving gif")

    # Saving a gif, since I can't view it on my IDE
    if isinstance(filename, type(None)):
        anim.save('output.gif', writer='imagemagick')
    else:
        anim.save(filename, writer="imagemagick")

    print("Done animating, gif saved, xoxo")
    return 0