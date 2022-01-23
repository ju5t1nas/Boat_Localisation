from numpy import ones, less_equal, greater_equal, where, sqrt, zeros, size
from scipy.stats import norm
from numpy.random import normal

def weights_improved(truePosX, truePosY, particlesx, particlesy, direction, index, map):
    # Moving true position back 
    old_true_PosX = truePosX[index-1] - direction[0]
    old_true_PosY = truePosY[index-1] - direction[1]

    # Moving particles back a previous direction
    old_part_x = particlesx - ones(len(particlesx))*direction[0]
    old_part_y = particlesy - ones(len(particlesy))*direction[1]

    # Examining Particles New
    less_x = less_equal(particlesx, 1)
    gret_x = greater_equal(particlesx, map.shape[1])
    bad_x = less_x + gret_x # finding bad particles

    less_y = less_equal(particlesy,1)
    gret_y = greater_equal(particlesy, map.shape[0])
    bad_y = less_y + gret_y # finding bad particles

    new_bad_particles = bad_x + bad_y # all bad particles

    # Examining Particles Old
    less_x = less_equal(old_part_x, 1)
    gret_x = greater_equal(old_part_x, map.shape[1])
    bad_x = less_x + gret_x # finding bad particles

    less_y = less_equal(old_part_y,1)
    gret_y = greater_equal(old_part_y, map.shape[0])
    bad_y = less_y + gret_y # finding bad particles

    old_bad_particles = bad_x + bad_y # all bad particles

    bad_particles = new_bad_particles + old_bad_particles
    good_array = where(bad_particles == False)[0]

    # Computing what previous was called epsilon
    particle_depths = map[particlesy[good_array],particlesx[good_array]]
    old_particle_depths = map[old_part_y[good_array].astype(int),old_part_x[good_array].astype(int)]

    true_depths = ones(len(particle_depths)) * map[int(truePosY[index-1]), int(truePosX[index-1])] + map[int(truePosY[index-1]), int(truePosX[index-1])]*normal(0,0.05)
    old_true_depths = ones(len(particle_depths)) * map[int(old_true_PosY), int(old_true_PosX)]
    
    depth_diff = true_depths - particle_depths

    change_depth_diff = (true_depths-old_true_depths) - (particle_depths - old_particle_depths)
    sigma = abs(sqrt(0.15)*map[int(truePosY[index-1]), int(truePosX[index-1])])

    good_weights = norm(0, sigma).pdf(depth_diff) * norm(0, 2*sigma).pdf(change_depth_diff)

    weights = zeros(len(particlesx))
    weights[good_array] = good_weights

    return weights