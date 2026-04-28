import numpy as np

# create arrays
a = np.array([1,2,3,4,5])
print(a)

## do math on every element
scores = np.array([70,80,90])
curved_scores = scores + 5
print(curved_scores)

## Multiply arrays element by element
prices = np.array([10, 20, 30])
quantities = np.array([2, 3, 4])

totals = prices * quantities
print(totals)

## Basic statistics
temperatures = np.array([72, 75, 70, 68, 74, 77, 73])

print("Mean:", np.mean(temperatures))
print("Minimum:", np.min(temperatures))
print("Maximum:", np.max(temperatures))
print("Standard deviation:", np.std(temperatures))

## Make arrays quickly
print(np.zeros(5))
print(np.ones(5))
print(np.arange(1, 11))
print(np.linspace(0, 1, 5))

## Two-dimensional arrays
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)
print("Shape:", matrix.shape)

## Indexing and slicing
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(matrix[0, 0])     # first row, first column
print(matrix[1, 2])     # second row, third column
print(matrix[:, 1])     # all rows, second column
print(matrix[1, :])     # second row, all columns


## Boolean filtering
ages = np.array([12, 17, 18, 21, 15, 30])

adults = ages[ages >= 18]
# equivalent in lists
adults = [age for age in ages if age>=18]

print(adults)

## Reshaping arrays
numbers = np.arange(1, 13)

grid = numbers.reshape(3, 4)

print(grid)

## A small real-world example: grades
grades = np.array([
    [85, 90, 88],
    [70, 75, 80],
    [95, 92, 96],
    [60, 65, 70]
])
# axis = 1 "each row", axis = 0 "each column"
student_averages = np.mean(grades, axis=1) 
exam_averages = np.mean(grades, axis=0)

print("Student averages:", student_averages)
print("Exam averages:", exam_averages)

##
x_values = np.arange(1, 6)
x_val = [1,2,3,4,5]
points = [(x, x**2) for x in x_values]
print(points)

##
x_values = np.arange(1, 6)

# List comprehension
squares_list = [x**2 for x in x_values]

# NumPy vectorized version
squares_array = x_values**2

print(squares_list)
print(squares_array)

## numpy array list comprehension
x_values = np.array([1, 2, 3, 4, 5])
squares = [x**2 for x in x_values]
print(squares)

# better implementation:
squares = x_values**2
print(squares)

## creating coordinate pairs
x_values = np.arange(1, 6)

points = [(x, x**2) for x in x_values]

print(points)

## filtering values
values = np.array([10, 15, 20, 25, 30])
large_values = [x for x in values if x > 20]
print(large_values)

# equivalent
large_values = values[values > 20]
print(large_values) 

## applying a function
angles = np.array([0, np.pi / 2, np.pi])
sines = [np.sin(angle) for angle in angles]
print(sines)

# equivalent
sines = np.sin(angles)
print(sines)

## distances from points
points = [(0, 0), (3, 4), (5, 12)]
distances = [np.sqrt(x**2 + y**2) for x, y in points]
print(distances)

# equivalent
points = np.array([
    [0, 0],
    [3, 4],
    [5, 12]
])

distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
print(distances)

####
# Make a new list
#[x**2 for x in numbers]

# Filter a list
#[x for x in numbers if x > 0]

# Work with tuples
#[x + y for x, y in points]

# Work with dictionaries
#[name for name, score in grades.items() if score >= 70]

# Read lines from a file
#[line.strip() for line in file]

# Use if-else
#["pass" if score >= 70 else "fail" for score in scores]

# Nested loops
#[(x, y) for x in xs for y in ys]