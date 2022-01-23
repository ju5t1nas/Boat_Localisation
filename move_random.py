from numpy.random import randint

def move_random(position, depth):
    direction = [randint(-1,2), randint(-1,2)]

    new_position =  [0,0]
    new_position[0] = position[0] + direction[0]
    new_position[1] = position[1] + direction[1]

    if (depth[int(new_position[1]), int(new_position[0])] >= -1):
        new_position = position
    
    return int(new_position[0]), int(new_position[1]), direction
