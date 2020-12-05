import math as m

puzzle_input = [line.strip() for line in open("input.txt")]

test = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def getRow(boarding_pass) -> int:
    min = 0
    max = 127
    length = 128
    for c in boarding_pass[:-3]:
        if c == "F":
            max = max - m.floor(length / 2)
            length = length / 2
        else:
            min = min + m.ceil(length / 2)
            length = length / 2

    if min == max:
        return min
    return -1


def getColumn(boarding_pass) -> int:
    min = 0
    max = 7
    length = 8
    for c in boarding_pass[-3:]:
        if c == "L":
            max = max - m.floor(length / 2)
            length = length / 2
        else:
            min = min + m.ceil(length / 2)
            length = length / 2

    if min == max:
        return min
    return -1


def getSeatID(boarding_pass):
    row = getRow(boarding_pass)
    col = getColumn(boarding_pass)
    return row * 8 + col


def checkInput(list, part2):
    ids = []
    for boarding_pass in list:
        ids.append(getSeatID(boarding_pass))

    if part2:
        res = []
        sorted_ids = sorted(ids)

        for seatid in sorted_ids:
            if not ((seatid-1) in sorted_ids and (seatid+1) in sorted_ids):
                res.append(seatid)

        return res
    return max(ids)


print(f"Part 1 - Max Seat ID: {checkInput(puzzle_input, False)}")
print(
    f"Part 2 - Seats with missing neighbors: {checkInput(puzzle_input, True)} -> 629")
