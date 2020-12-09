puzzle_input_test = [int(line) for line in open("testinput.txt")]
puzzle_input = [int(line) for line in open("input.txt")]


def part_1(nums, preamble):
    start = 0
    res = None

    next_nums = nums[preamble:]
    for num in next_nums:
        found = False
        prev_nums = nums[start:preamble]

        for i in range(0, len(prev_nums)):
            for j in range(i, len(prev_nums)):
                if prev_nums[i] + prev_nums[j] == num:
                    found = True
                    break

        if found == False:
            res = num
            break

        preamble += 1
        start += 1

    return res


def part_2(nums, preamble):
    lower = 0
    upper = 0
    insecure = part_1(nums, preamble)

    val = nums[lower]

    while val != insecure:
        if val < insecure:
            upper += 1
            val += nums[upper]
        elif val > insecure:
            val -= nums[lower]
            lower += 1

    return min(nums[lower:upper]) + max(nums[lower:upper])


part_1_res = part_1(puzzle_input, 25)
part_2_res = part_2(puzzle_input, 25)

print(f"Part 1 - First Weakness: {part_1_res}")
print(f"Part 2 - Solution: {part_2_res}")
