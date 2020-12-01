def read_input(filename) -> list[int]:
    res = []
    with open(filename, "r") as f:
        for line in f:
            res.append(int(line.strip()))

    return res

# For Part 1


def getPair(pNums):
    for i in range(0, len(pNums)):
        for j in range(1, len(pNums)):
            if pNums[i] + pNums[j] == 2020:
                return (pNums[i], pNums[j], pNums[i]*pNums[j])

# For Part 2


def getTriple(pNums):
    for i in range(0, len(pNums)):
        for j in range(1, len(pNums)):
            for x in range(2, len(pNums)):
                if pNums[i] + pNums[j] + pNums[x] == 2020:
                    return (pNums[i], pNums[j], pNums[x], pNums[i] * pNums[j] + pNums[x])


# Read input
nums = read_input("input.txt")

# Solutions
a, b, productPair = getPair(nums)
c, d, e, productTriple = getTriple(nums)

print(f"Part 1 - Pair is ({a},{b}) and solution is: {productPair}")
print(f"Part 2 - Triple is ({e},{d},{e}) and solution is: {productTriple}")
