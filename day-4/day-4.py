import re


def parse_raw_input(raw_input):
    res = []

    passport = {}
    for i in range(0, len(raw_input)):
        split_line = raw_input[i].split(" ")

        if raw_input[i] == "":
            res.append(passport)
            passport = {}
            continue

        for entry in split_line:
            key = entry.split(":")[0]
            val = entry.split(":")[1]
            passport[key] = val

    res.append(passport)

    return res


# Valid Keys
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validatePassportKeys(passport) -> bool:
    passport_keys = passport.keys()
    checks = 0
    for key in passport_keys:
        if key in keys:
            checks += 1
    if checks == 7:
        return True
    return False


def checkAllPassports(passports, part2) -> int:
    valid_passports = 0
    for passport in passports:
        if validatePassportKeys(passport):
            if part2:
                if validatePassportValues(passport):
                    valid_passports += 1
            else:
                valid_passports += 1

    return valid_passports

# Works only if all keys have been validated


def validatePassportValues(passport) -> bool:
    if not (int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002):
        return False

    if not (int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020):
        return False

    if not (int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030):
        return False

    if passport["hgt"][-2:] == "cm":
        if not(int(passport["hgt"][:-2]) >= 150 and int(passport["hgt"][:-2]) <= 193):
            return False
    elif passport["hgt"][-2:] == "in":
        if not (int(passport["hgt"][:-2]) >= 59 and int(passport["hgt"][:-2]) <= 76):
            return False
    else:
        return False

    re_haircolor = r"#[0-9|a-f]{6}"

    match = re.search(re_haircolor, passport["hcl"])
    if match == None or len(match.string) != 7:
        return False

    if not (passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return False

    re_pid = r"[0-9]{9}"

    match = re.search(re_pid, passport["pid"])
    if match == None or len(match.string) != 9:
        return False

    return True


puzzle_input_raw = [line.strip() for line in open("input.txt")]
puzzle_input = parse_raw_input(puzzle_input_raw)

print(f"Part 1 - Valid Passports: {checkAllPassports(puzzle_input, False)}")
print(f"Part 2 - Valid Passports: {checkAllPassports(puzzle_input, True)}")
