def read_input(filename):
    res = []
    with open(filename, "r") as f:
        for line in f:
            split_line = line.strip().split(" ")

            res.append({
                "amount": {
                    "min": split_line[0].split("-")[0],
                    "max": split_line[0].split("-")[1],
                },
                "letter": split_line[1][0],
                "password": split_line[2],
            })

        return res

# Checks if given entry is valid (part 1)


def checkIfValidPassword_part_1(entry) -> bool:
    letter = entry.get("letter")
    count_letter = 0

    amount_min = int(entry.get("amount").get("min"))
    amount_max = int(entry.get("amount").get("max"))

    for c in entry.get("password"):
        if c == letter:
            count_letter += 1

    if count_letter >= amount_min and count_letter <= amount_max:
        return True
    return False

# Checks if given entry is valid (part 2)


def checkIfValidPassword_part_2(entry) -> bool:
    letter = entry.get("letter")

    index_one = int(entry.get("amount").get("min")) - 1
    index_two = int(entry.get("amount").get("max")) - 1

    password = entry.get("password")

    if password[index_one] == letter and password[index_two] == letter:
        return False

    if password[index_one] == letter or password[index_two] == letter:
        return True

    return False

# Counts all valid passwords (part 1)


def checkAllEntries_part_1(entries):
    count_valid_passwords = 0

    for entry in entries:
        if checkIfValidPassword_part_1(entry):
            count_valid_passwords += 1

    return count_valid_passwords

# Counts all valid passwords (part 2)


def checkAllEntries_part_2(entries):
    count_valid_passwords = 0

    for entry in entries:
        if checkIfValidPassword_part_2(entry):
            count_valid_passwords += 1

    return count_valid_passwords


puzzle_input = read_input("input.txt")
valid_passwords_part_1 = checkAllEntries_part_1(puzzle_input)
valid_passwords_part_2 = checkAllEntries_part_2(puzzle_input)

print(f"Part 1 - Amount of valid passwords: {valid_passwords_part_1}")
print(f"Part 2 - Amount of valid passwords: {valid_passwords_part_2}")
