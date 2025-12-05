"""Module providing a function printing X O game"""

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
game_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

for x in range(0, 5):
    position = input("Where do you want to put the ❌ marker?")

    column_w = int(position[0])
    row_w = int(position[1])

    # accounting for the zwro index
    # column = column_w - 1
    # row = row_w - 1

    # wanted_row = game_map[row_w - 1]
    # wanted_row[column_w - 1] = "❌"

    game_map[row_w - 1][column_w - 1] = "❌"

    print(f"{row1}\n{row2}\n{row3}")

    position = input("Where do you want to put the ⭕️ marker?")

    column_w = int(position[0])
    row_w = int(position[1])

    # accounting for the zwro index
    column = column_w - 1
    row = row_w - 1

    wanted_row = game_map[row]
    wanted_row[column] = "⭕️"

    print(f"{row1}\n{row2}\n{row3}")
