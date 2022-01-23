from numpy import arange, meshgrid

def particles_grid(map, spacing = None):
    if spacing is None:
        x = arange(1, map.shape[1], 1)
        y = arange(1, map.shape[0], 1)
    else:
        x = arange(1, map.shape[1], spacing)
        y = arange(1, map.shape[0], spacing)

    xx, yy = meshgrid(x, y, indexing='xy')

    return xx.flatten(), yy.flatten()