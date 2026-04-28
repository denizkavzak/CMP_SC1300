# List comprehension
# new_list = [expression for item in iterable]

x_values = [1, 2, 3, 4, 5]
squares = []
for x in x_values:
    squares.append(x**2)
print(squares)

## basic pattern
x_values = [1, 2, 3, 4, 5]
squares = [x**2 for x in x_values]
print(squares)

##
x_values = [1, 2, 3, 4, 5]
points = [(x, x**2) for x in x_values]
print(points)

# same as
points = []
for x in x_values:
    if x%2 == 0:
        points.append((x, x**2))

print(points)

##
x_values = [1, 2, 3, 4, 5, 6]
even_squares = [x**2 for x in x_values if x % 2 == 0]
print(even_squares)

##
## What with does?
# 1. Open scores.txt in read mode ("r")
# 2. Store the opened file object in the variable file
# 3. Run the indented code under it
# 4. Automatically close the file afterward, even if an error happens

# reading lines from a file
with open("students.txt", "r") as file:
    students = [line.strip() for line in file]

print(students)

## Reading only certain lines from a file
with open("scores.txt", "r") as file:
    lines = [line.strip() for line in file]

passed = [line for line in lines if int(line.split(",")[1]) >= 70]

print(passed)

## Turning file lines into tuples
with open("scores.txt", "r") as file:
    records = [line.strip().split(",") for line in file]

records = [(name, int(score)) for name, score in records]

print(records)