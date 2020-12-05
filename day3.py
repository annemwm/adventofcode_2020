from functools import reduce

# data setup
with open("input.txt", "r") as f:
    data = f.read()

data = [d for d in data.split("\n") if d]
matrix = [[c for c in string] for string in data]
row_length = len(matrix[0])
max_row_index = len(matrix) - 1  # do checks outside of move to see if we're there


def move(row, column, row_move, column_move):
    row = row + row_move
    column = (column + column_move) % row_length

    return row, column


def is_tree(hill_map, row, column):
    return hill_map[row][column] == '#'


def check_trees_on_map(row_move, column_move):
    row, column = 0, 0
    tree_count = 0
    while row <= max_row_index:
        if is_tree(matrix, row, column):
            tree_count += 1
        row, column = move(row, column, row_move, column_move)

    return tree_count


print(check_trees_on_map(1, 3))

# part 2
all_routes = [check_trees_on_map(1, 1), check_trees_on_map(3, 1), check_trees_on_map(1, 5),
              check_trees_on_map(1, 7), check_trees_on_map(2, 1)]
print(reduce(lambda x, y: x*y, all_routes))
