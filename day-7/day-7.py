def read_puzzle_input(filename):
    res = []

    for line in open(filename, 'r'):
        [first_half, second_half] = line.split("contain")

        rule = {
            "color": first_half[:-6],
            "contents": []
        }

        split_contents = [item.strip() for item in second_half.split("bag")]
        del split_contents[len(split_contents)-1]

        for bag in split_contents:
            if bag.startswith(", "):
                amount = bag[2:].split(" ", 1)[0]
                color = bag[2:].split(" ", 1)[1]
                rule["contents"].append(
                    {
                        "color": color,
                        "amount": amount
                    }
                )
            elif bag.startswith("s, "):
                amount = bag[3:].split(" ", 1)[0]
                color = bag[3:].split(" ", 1)[1]
                rule["contents"].append(
                    {
                        "color": color,
                        "amount": amount
                    }
                )
            elif not bag.startswith("no other"):
                [amount, color] = bag.split(" ", 1)
                rule["contents"].append({
                    "color": color,
                    "amount": amount
                })

        res.append(rule)

    return res


def is_color_in_bag_direct(color_rule):
    color = "shiny gold"
    for x in color_rule["contents"]:
        if x["color"] == color:
            return True
    return False


def direct_match(rules):
    return set([color["color"] for color in list(filter(is_color_in_bag_direct, rules))])


def indirect_match(rules, colors):
    # Cast a list from the copied set
    res = list(colors)

    # Loop through the found colors
    for color in res:
        # And rules
        for rule in rules:
            # And the contents
            for rule_color in rule["contents"]:
                if rule_color["color"] == color:
                    # Add the bag to the list
                    colors.add(rule["color"])

    # Same length => return False and break main loop
    if len(res) == len(colors):
        return False, colors
    return True, colors


def get_indirect_matches(rules):
    # Get the Direct Matches
    direct = direct_match(puzzle_input)
    while True:
        # Get a batch of indirect matches
        [found_more, bags] = indirect_match(rules, direct)

        # If more matches were not found break loop and return
        if not found_more:
            break

        # Add the newly found bags and add them to the direct set
        for bag in bags:
            direct.add(bag)

    # Return the amount of bags found
    return len(direct)


puzzle_input = read_puzzle_input("input.txt")
print(
    f"Part 1 - Amount of Bags possible: {get_indirect_matches(puzzle_input)}")
