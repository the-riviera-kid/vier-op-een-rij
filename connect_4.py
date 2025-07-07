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


def get_row(grid, coordination):
    if grid != []:
        return (1, 2)
