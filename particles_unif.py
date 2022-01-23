from numpy.random import randint
from numpy import size

def particles_unif(map, number_of_part = None):

    if number_of_part is None: # If number of particles is unspecified, we use 5% of the map size.
        xx = randint(1,map.shape[1], size = round(size(map)*0.05)) # number of columns is x
        yy = randint(1,map.shape[0], size = round(size(map)*0.05)) # number of rows is y
    else:
        xx = randint(1,map.shape[1], size = number_of_part) # number of columns is x
        yy = randint(1,map.shape[0], size = number_of_part) # number of rows is y
    
    return xx, yy