# Day 6 - Custom Customs

## Part 1

### Task

As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

```bash
abcx
abcy
abcz
```

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

```bash
abc

a
b
c

ab
ac

a
a
a
a

b
```

This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". **What is the sum of those counts?**

### My Solution

Go through each group and add each answer to a set. Then return the length of that set and sum each group length up.

**My puzzle answer was 6532.**

## Part 2

### Task

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

```bash
abc

a
b
c

ab
ac

a
a
a
a

b
```

This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". **What is the sum of those counts?**

### My Solution

I then created a dictionary with all chars as keys and added the id oh each person in the group to a list that corresponds to 
the char. I then compare the lengths of each chars list and the group list to check if everyone has answered yes to that question.

**My puzzle answer was 3427.**

## Things learned from this
---

```python
1 data = open("input.txt").read().split("\n\n")
2 set(entry.replace("\n", "")
```

This would've have split up the text in to the important parts.
Then each entry would have some newlines in *line 2* takes care of those and would create a set.
Sets of a string **automatically treat a character as a member and de duplicates them**.

Summing the length of each of these entries would have gotten me the star for part 1 in a single line.

```python
sum([len(set(entry.replace("\n",""))) for entry in open("input.txt").read().split("\n\n")])
```

### For Part 2

```python
items = entry.split()
set.intersection(*[set(item) for item in items])
```

The * indicates destructuring or "splatting" and allowing us to pass an variable amount of arguments to intersection.

>The * here is the "splat" operator, which means "unpack this list, and use each of its members as arguments to the function". The terminology is somewhat unclear here, some call it "splat", some call it "unpack", some call it "destructure", some call it "expanding".

**So part 2 could have been done like:**

```python
total = 0
for entry in data:
    items = entry.split()
    common = set.intersection(*map(set, items))
    total += len(common)
print("total", total)
```
