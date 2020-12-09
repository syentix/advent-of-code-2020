puzzle_input_test = [int(line) for line in open("testinput.txt")]
puzzle_input = [int(line) for line in open("input.txt")]


def part_1(nums):
    preamble = 25
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


def part_2(nums):
    start = 0
    stop = 0
    insecure = part_1(nums)

    for i in range(0, len(nums)):
        if sum(nums[start:i]) == insecure:
            stop = i
    pass


part_1_res = part_1(puzzle_input)
#part_2_res = part_2(puzzle_input_test)

print(f"Part 1 - First Vulnrability: {part_1_res}")
#print(f"Part 2 - First Vulnrability: {part_2_res}")
