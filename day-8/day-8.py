def read_instructions(filename):
    res = []
    for line in open(filename, "r"):
        [op, val] = line.strip().split(" ", 1)
        res.append({
            "op": op,
            "val": val
        })

    return res


def handheld_device_part_1(instructions):
    acc = 0
    programm_lines = []

    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        if i in programm_lines:
            return acc
        programm_lines.append(i)
        if instruction["op"] == "acc":
            acc += int(instruction["val"])

        if instruction["op"] == "jmp":
            i += int(instruction["val"])
        else:
            i += 1


def does_it_loop(instructions):
    acc = 0
    programm_lines = []

    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        if i in programm_lines:
            return True, acc
        programm_lines.append(i)
        if instruction["op"] == "acc":
            acc += int(instruction["val"])

        if instruction["op"] == "jmp":
            i += int(instruction["val"])
        else:
            i += 1

    return False, acc


def part_2(instructions):
    nops_jmps_indexes = []
    for i in range(0, len(instructions)):
        instruction = instructions[i]
        if instruction["op"] == "jmp" or instruction["op"] == "nop":
            new_instruction = {}
            if instruction["op"] == "nop":
                new_instruction = {
                    "op": "jmp",
                    "val": instruction["val"],
                }
            else:
                new_instruction = {
                    "op": "nop",
                    "val": instruction["val"],
                }
            nops_jmps_indexes.append({
                "index": i,
                "new_instruction": new_instruction
            })

    for new_instruction in nops_jmps_indexes:
        new_input = instructions.copy()
        new_input[new_instruction["index"]
                  ] = new_instruction["new_instruction"]
        looped, acc = does_it_loop(new_input)
        if not looped:
            return acc


puzzle_input = read_instructions("input.txt")
part_1 = handheld_device_part_1(puzzle_input)
part_2 = part_2(puzzle_input)
print(f"Part 1 - Accumulator before endless loop: {part_1}")
print(f"Part 2 - Accumulator modified: {part_2}")
