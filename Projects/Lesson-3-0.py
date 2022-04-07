import random

START_P = 12
FINISH_P = 24
ROAD_I = 1
WALL_P = 0

map = [
    [START_P, ROAD_I, ROAD_I, ROAD_I, ROAD_I],
    [WALL_P, ROAD_I, WALL_P, WALL_P, ROAD_I],
    [WALL_P, ROAD_I, WALL_P, WALL_P, ROAD_I],
    [WALL_P, ROAD_I, WALL_P, WALL_P, ROAD_I],
    [WALL_P, ROAD_I, ROAD_I, FINISH_P, FINISH_P]
]

start_pos_y = 0
start_pos_x = 0
finish_pos = 0

y_rows = 5
x_rows = 5

def get_pos(current_pos_y, current_pos_x):
    random_number = random.random()

    can_go_right = current_pos_x+1<x_rows and map[current_pos_y][current_pos_x+1] == ROAD_I
    can_go_left = current_pos_x-1 >= 0 and map[current_pos_y][current_pos_x-1] == ROAD_I
    can_go_top = current_pos_y-1 >= 0 and map[current_pos_y-1][current_pos_x] == ROAD_I
    can_go_down = current_pos_y+1 < y_rows and map[current_pos_y+1][current_pos_x] == ROAD_I

    finish_go_right = current_pos_x+1<x_rows and map[current_pos_y][current_pos_x+1] == FINISH_P
    finish_go_left = current_pos_x-1 >= 0 and map[current_pos_y][current_pos_x-1] == FINISH_P
    finish_go_top = current_pos_y-1 >= 0 and map[current_pos_y-1][current_pos_x] == FINISH_P
    finish_go_down = current_pos_y+1 < y_rows and map[current_pos_y+1][current_pos_x] == FINISH_P

    avaliabe_pos = []


    if can_go_right:
        print("Can go right")
        position_on_right = [current_pos_y, current_pos_x+1]
        avaliabe_pos.append(position_on_right)

    if can_go_left:
        print("Can go left")
        position_on_left = [current_pos_y, current_pos_x-1]
        avaliabe_pos.append(position_on_left)

    if can_go_down:
        print("Can go down")
        position_on_down = [current_pos_y+1, current_pos_x]
        avaliabe_pos.append(position_on_down)

    if can_go_top:
        print("Can go up")
        position_on_up = [current_pos_y-1, current_pos_x]
        avaliabe_pos.append(position_on_up)

    if finish_go_down:
        print("The end")
        print("[",current_pos_y +1,"]", "[",current_pos_x,"]")
        quit()
    if finish_go_top:
        print("The end")
        print("[",current_pos_y -1,"]", "[",current_pos_x,"]")
        quit()
    if finish_go_right:
        print("The end")
        print("[",current_pos_y,"]", "[",current_pos_x+1,"]")
        quit()
    if finish_go_left:
        print("The end")
        print("[",current_pos_y,"]", "[",current_pos_x-1,"]")
        quit()



    return random.choice(avaliabe_pos)

next_pos = get_pos(start_pos_y, start_pos_x)
print("Next free position is: ", next_pos)

while next_pos:

    next_pos = get_pos(next_pos[0], next_pos[1])
    print("Next free position is: ", next_pos)

    