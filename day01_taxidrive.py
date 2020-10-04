"""
https://adventofcode.com/2016/day/1
"""

from typing import Callable, List, NamedTuple

TEST_INPUT_1 = 'R2, L3'
TEST_INPUT_2 = 'R2, R2, R2'
TEST_INPUT_3 = 'L100, R100'

# # PSEUDOCODE FOR R2, L3
# START =  (0, 0)
# STEP_1 = (2, 0)
# STEP_2 = (2, 3)
# print(abs(0-2) + abs(0-3))

# # PSEUDOCODE FOR R2, R2, R2
# START =  (0, 0)
# STEP_1 = (2, 0)
# STEP_2 = (2, -2)
# STEP_3 = (0, -2)
# print(abs(0-0) + abs(0-2))

# # PSEUDOCODE FOR R5, L5, R5, R3
# START =  (0, 0)
# STEP_1 = (5, 0)
# STEP_2 = (5, 5)
# STEP_3 = (10, 5)
# STEP_4 = (10, 2)
# print(abs(0-10) + abs(0-2))

def sequence_route(sequence: str) -> List[str]:
    steps = sequence.split(', ')
    return steps


def use_compass(orientation: str, direction: str) -> str:
    new_orientation = ''

    if orientation == 'NORTH' and direction == 'R':
        new_orientation = 'EAST'
    elif orientation == 'NORTH' and direction == 'L':
        new_orientation = 'WEST'

    elif orientation == 'EAST' and direction == 'R':
        new_orientation = 'SOUTH'
    elif orientation == 'EAST' and direction == 'L':
        new_orientation = 'NORTH'

    elif orientation == 'SOUTH' and direction == 'R':
        new_orientation = 'WEST'
    elif orientation == 'SOUTH' and direction == 'L':
        new_orientation = 'EAST'

    elif orientation == 'WEST' and direction == 'R':
        new_orientation = 'NORTH'
    elif orientation == 'WEST' and direction == 'L':
        new_orientation = 'SOUTH'

    return new_orientation


def walk(start_point, orientation: str, direction: str, num_steps: int):

    if orientation == 'NORTH' and direction == 'R':
        start_point[0] += num_steps
        start_point[1] = start_point[1]

    elif orientation == 'NORTH' and direction == 'L':
        start_point[0] -= num_steps
        start_point[1] = start_point[1]

    elif orientation == 'EAST' and direction == 'R':
        start_point[0] = start_point[0]
        start_point[1] -= num_steps

    elif orientation == 'EAST' and direction == 'L':
        start_point[0] = start_point[0]
        start_point[1] += num_steps

    elif orientation == 'SOUTH' and direction == 'R':
        start_point[0] -= num_steps
        start_point[1] = start_point[1]

    elif orientation == 'SOUTH' and direction == 'L':
        start_point[0] += num_steps
        start_point[1] = start_point[1]

    elif orientation == 'WEST' and direction == 'R':
        start_point[0] = start_point[0]
        start_point[1] += num_steps

    elif orientation == 'WEST' and direction == 'L':
        start_point[0] = start_point[0]
        start_point[1] -= num_steps

    return start_point


def navigate(sequence: List[str]) -> int:
    start_point = [0, 0]
    end_point = [0, 0]
    orientation = 'NORTH'
    print(f'Start configuration: You are at {start_point} and you are facing towards {orientation}.')

    for i, item in enumerate(sequence):
        direction = item[0]
        num_steps = int(item[1:])
        end_point = walk(end_point, orientation, direction, num_steps)
        orientation = use_compass(orientation, direction)
        print(f"After step {i} you've turned to your {direction} and took {num_steps} steps. So now you are at {end_point} and facing towards {orientation}.")

    distance_hq_bunny = abs(start_point[0] - end_point[0]) + abs(start_point[1] - end_point[1])

    return distance_hq_bunny

step_one = navigate(sequence_route(TEST_INPUT_1))

step_two = navigate(sequence_route(TEST_INPUT_2))

step_three = navigate(sequence_route(TEST_INPUT_3))

# Test cases Part One
assert navigate(sequence_route('R2, L3')) == 5
assert navigate(sequence_route('R2, R2, R2')) == 2
assert navigate(sequence_route('R5, L5, R5, R3')) == 12
assert navigate(sequence_route(TEST_INPUT_3)) == abs(-100 - 0) + abs(0-100)

if __name__ == '__main__':
    with open('day01_input.txt', 'r') as f:
        document = f.read().strip()
        distance_bunny_hq = navigate(sequence_route(document))
        print(distance_bunny_hq)

