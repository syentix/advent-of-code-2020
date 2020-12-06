def read_input_raw(filename):
    res = []
    lineres = []
    for line in open(filename, 'r'):
        if line.strip() == "":
            res.append(lineres)
            lineres = []
        else:
            lineres.append(line.strip())

    res.append(lineres)
    return res


def get_unique_answers_len(group):
    res = set()
    for person in group:
        for answer in person:
            res.add(answer)

    return len(res)


def get_unique_answers_len_part_2(group):
    res = {}
    count = 0
    for i in range(0, len(group)):
        for answer in group[i]:
            for c in answer:
                if c in res.keys():
                    res[c].append(i)
                else:
                    res.setdefault(c, [i])
    for val in res.values():
        if len(val) == len(group):
            count += 1

    return count


def get_number_of_answers_puzzle_input(puzzle_input, part2):
    res = 0
    if part2:
        for group in puzzle_input:
            res += get_unique_answers_len_part_2(group)
    else:
        for group in puzzle_input:
            res += get_unique_answers_len(group)

    return res


test_input = read_input_raw("input.txt")

print(
    f"Part 1 - Sum of all answers: {get_number_of_answers_puzzle_input(test_input, False)}")
print(
    f"Part 2 - Sum of all answers: {get_number_of_answers_puzzle_input(test_input, True)}")
