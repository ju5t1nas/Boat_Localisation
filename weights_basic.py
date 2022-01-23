from numpy import less_equal, greater_equal, where, sqrt, ones, zeros
from numpy.random import normal
from scipy.stats import norm

def weights_basic(truePosX, truePosY, particlesx, particlesy, index, map):
    # Examining Particles
    less_x = less_equal(particlesx, 1)
    gret_x = greater_equal(particlesx, map.shape[1])
    bad_x = less_x + gret_x # finding bad particles

    less_y = less_equal(particlesy,1)
    gret_y = greater_equal(particlesy, map.shape[0])
    bad_y = less_y + gret_y # finding bad particles

    bad_particles = bad_x + bad_y # all bad particles

    good_array = where(bad_particles == False)[0]

    # Computing what previous was called epsilon
    particle_depths = map[particlesy[good_array],particlesx[good_array]]
    sigma = abs(sqrt(0.15)*map[int(truePosY[index-1]), int(truePosX[index-1])])
    true_depths = ones(len(particle_depths)) * map[int(truePosY[index-1]), int(truePosX[index-1])] + normal(0,sigma)
    depth_diff = true_depths - particle_depths

    good_weights = norm(0, sigma).pdf(depth_diff)

    weights = zeros(len(particlesx))
    weights[good_array] = good_weights
    
    return weights