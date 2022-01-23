def move_DVD(position, direction, map):

    new_position =  [0,0]
    new_position[0] = position[0] + direction[0]
    new_position[1] = position[1] + direction[1]

    Up_Left = [-1,1]
    Up_Right = [1,1]
    Dw_Left = [-1,-1]
    Dw_Right = [1,-1]

    if (map[int(new_position[1]), int(new_position[0])] >= -1):
        
        # Left edge bounce:
        if (map[int(position[1]), int(new_position[0])] >= -1) and direction == Up_Left:
            direction = Up_Right
            new_position = position
        elif (map[int(position[1]), int(new_position[0])] >= -1) and direction == Dw_Left:
            direction = Dw_Right
            new_position = position

        # Right edge bounce:
        elif (map[int(position[1]), int(new_position[0])] >= -1) and direction == Up_Right:
            direction = Up_Left
            new_position = position

        elif (map[int(position[1]), int(new_position[0])] >= -1) and direction == Dw_Right:
            direction = Dw_Left
            new_position = position

        # Top edge bounce:
        elif (map[int(new_position[1]), int(position[0])] >= -1) and direction == Up_Right:
            direction = Dw_Right
            new_position = position

        elif (map[int(new_position[1]), int(position[0])] >= -1) and direction == Up_Left:
            direction = Dw_Left
            new_position = position

        # Bottom edge bounce:
        elif (map[int(new_position[1]), int(position[0])] >= -1) and direction == Dw_Right:
            direction = Up_Right
            new_position = position

        elif (map[int(new_position[1]), int(position[0])] >= -1) and direction == Dw_Left:
            direction = Up_Left
            new_position = position

    return int(new_position[0]), int(new_position[1]), direction