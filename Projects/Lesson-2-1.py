import random


map = [
    [12, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1]
]

start_pos_y = 0
start_pos_x = 0
finish_pos = 0

y_rows = 5
x_rows = 5


def get_next_pos(current_pos_y, current_pos_x):
    if current_pos_y == 4 and current_pos_x == 4:
        print("End")
        quit()
    random_number = random.random()
    print (random_number)

    can_go_right = current_pos_x+1<x_rows and map[current_pos_y][current_pos_x+1] == 1
    can_go_left = current_pos_x-1 >= 0 and map[current_pos_y][current_pos_x-1] == 1
    can_go_top = current_pos_y-1 >= 0 and map[current_pos_y-1][current_pos_x] == 1
    can_go_down = current_pos_y+1 < y_rows and map[current_pos_y+1][current_pos_x] == 1
    while current_pos_x == current_pos_x and current_pos_y == current_pos_y:
        random_number = random.random()
        if can_go_left and random_number > 0.25 and random_number < 0.50:
            print("Can go left")
            return[current_pos_y, current_pos_x-1]
        elif can_go_right and random_number > 0.50 and random_number < 0.75:
            print("Can go right")
            return [current_pos_y, current_pos_x+1]
        elif can_go_top and random_number <0.25:
            print("Can go top")
            return[current_pos_y-1 , current_pos_x ]
        elif can_go_down and random_number >0.75:
            print("Can go down")
            return[current_pos_y + 1, current_pos_x]
    #if current_pos_y+1 < y_rows and map[current_pos_y+1][current_pos_x] == 1:
    #    print("You can go bottom") 
    #    return[current_pos_y+1 , current_pos_x ]
    #if current_pos_y-1 > 0 and map[current_pos_y-1][current_pos_x] == 1:
    #    print("You can go up") 
    #    return[current_pos_y-1 , current_pos_x ]
    #if current_pos_x+1<x_rows and map[current_pos_y][current_pos_x+1] == 1:
    #    print("You can go right.")
    #    return [current_pos_y, current_pos_x+1]
    #if current_pos_x-1 > 0 and map[current_pos_y][current_pos_x-1] == 1:
    #    print("You can go left") 
    #    return[current_pos_y, current_pos_x-1]

next_pos = get_next_pos(start_pos_y, start_pos_x)
print("Next free position is: ", next_pos)

while next_pos:
    next_pos = get_next_pos(next_pos[0], next_pos[1])
    print("Next free position is: ", next_pos)
