
map = [
    [12, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [24, 0, 1, 0, 0],
    [1, 1, 1, 1, 1]
]

start_pos_y = 0
start_pos_x = 0
finish_pos = 0

y_rows = 5
x_rows = 5
def get_next_pos(current_pos_y, current_pos_x):
    if current_pos_y+1 < y_rows and map[current_pos_y+1][current_pos_x] == 1:
        print("You can go bottom") 
        return[current_pos_y+1 , current_pos_x ]
    if current_pos_y-1 > 0 and map[current_pos_y-1][current_pos_x] == 1:
        print("You can go up") 
        return[current_pos_y-1 , current_pos_x ]
    if current_pos_x+1<x_rows and map[current_pos_y][current_pos_x+1] == 1:
        print("You can go right.")
        return [current_pos_y, current_pos_x+1]
    if current_pos_x-1 > 0 and map[current_pos_y][current_pos_x-1] == 1:
        print("You can go left") 
        return[current_pos_y, current_pos_x-1]
    if current_pos_y+1 < y_rows and map[current_pos_y+1][current_pos_x] == 1:
        print("You can go bottom") 
        return[current_pos_y+1 , current_pos_x ]

next_pos = get_next_pos(start_pos_y, start_pos_x)
print("Next free position is: ", next_pos)

while next_pos:
    next_pos = get_next_pos(next_pos[0], next_pos[1])
    print("Next free position is: ", next_pos)
