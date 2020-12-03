def read_input(filename):
    res = []
    with open(filename, "r") as f:
        for line in f:
            res.append(line.strip())

        return res


# def traverseSlopes(slope, right, down):
#     trees_encountered = 0
#     pos = 0

#     for i in range(0, len(slope)-1):

#         if i + down > len(slope) - 1:
#             return trees_encountered

#         if (pos + right) > (len(slope[i+down]) - 1):
#             current_pos = pos
#             overflow = ((len(slope[i+down]) - 1) - current_pos)

#             if right > 1:
#                 pos = (right - overflow) - 1
#             else:
#                 pos = 0
#
#         else:
#             pos = pos + 3

#         if slope[i+down][pos] == "#":
#             trees_encountered += 1

#     return trees_encountered


def traverseSlopes(slope, right, down):
    # Create Variables
    trees_encountered = 0
    # Using X as the X position in line
    x = 0

    # Using Y as line index and stepping by number of lines given through down
    for y in range(0, len(slope), down):
        if slope[y][x] == "#":
            trees_encountered += 1
        # Setting X as the modulo of (x + right) by the length of each line
        x = (x + right) % len(slope[y])

    return trees_encountered


puzzle_input = read_input("input.txt")

print(f"Slope 1: {traverseSlopes(puzzle_input, 1, 1)}")
print(f"Slope 2: {traverseSlopes(puzzle_input, 3, 1)}")
print(f"Slope 3: {traverseSlopes(puzzle_input, 5, 1)}")
print(f"Slope 4: {traverseSlopes(puzzle_input, 7, 1)}")
print(f"Slope 5: {traverseSlopes(puzzle_input, 1, 2)}")

print(f"Trees encountered: {traverseSlopes(puzzle_input, 1, 1) * traverseSlopes(puzzle_input, 3, 1) * traverseSlopes(puzzle_input, 5, 1) * traverseSlopes(puzzle_input, 7, 1) * traverseSlopes(puzzle_input, 1, 2)}")
