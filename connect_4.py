# Write a function which, given a sequence of elements and a target element,
# returns True if:
# - the target element is found
# - in four
# - consecutive locations,
# False otherwise.

def connect_4(sequence, target_element):
    count = 0
    for i in sequence:
        if i == target_element:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False

# Write a function which, given a grid and a set of coordinates
# representing a location within that grid, returns the row
# containing that position. If it cannot return a valid row,
# it should return None.
def get_row(grid, coordinates):
    column_number, row_number = coordinates
    if len(grid) > row_number:
        row = grid[row_number]
        if column_number < len(row):
            return row
    return None


# Write a function which, given a grid and a set of coordinates
# representing a location within that grid, returns the column
# containing that position. If it cannot return a valid column,
# it should return None.
def  get_column(grid, coordinates):
    column_number, row_number = coordinates
    if len(grid) >= row_number and len(grid[0]) >= column_number:
        column = [row[column_number] for row in grid]
        return column
    else:
        return None


# Write a function which, given a grid and a set of coordinates
# representing a location within that grid, returns a sequence
# of elements contained within a diagonal line that passes through
# the given location. This will be from the upper-left to the
# lower-right, like a backslash \. This diagonal will be at a
# 45 degree angle. If it cannot return a valid backslash diagonal,
# it should return None.
def get_diagonal_back_slash(grid, coordinates):
    column_number, row_number = coordinates
    if grid:
        diagonal = []
        for x in range(len(grid)):
            if len(grid) > row_number + x:
                diagonal.append(grid[row_number + x][column_number + x])
        return diagonal
    else:
        return None
