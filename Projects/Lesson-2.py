map = [
    [2, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 3]
]

start_pos_x = 0
start_pos_y = 0
finish_pos = 0

if map[0][1] == 1:
    print("You can go right.")

if map[1][0] == 1:
    print("You can go bottom")
