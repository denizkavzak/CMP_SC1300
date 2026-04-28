## getting values from tuples
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
x_values = [x for x, y in points]

print(x_values)

##
sums = [x + y for x, y in points]

print(sums)

## filtering tuples
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

large_x_points = [(x, y) for x, y in points if x > 3]

print(large_x_points)

## working with dictionaries
grades = {
    "Alice": 85,
    "Bob": 72,
    "Carlos": 91,
    "Diana": 64
}

names = [name for name in grades]
print(names)

scores = [score for score in grades.values()]
print(scores)

pairs = [(name, score) for name, score in grades.items()]
print(pairs)

# Filtering dictionaries with list comprehensions
passing_students = [name for name, score in grades.items() if score >= 70]
print(passing_students)

# get scores above 80
high_scores = [score for score in grades.values() if score > 80]
print(high_scores)

## The f makes it an f-string, which lets you put variables directly inside a string using {}.
messages = [f"{name} scored {score}" for name, score in grades.items()]

print(messages)
# eqivalent 
messages = ["%s scored %d" % (name, score) for name, score in grades.items()]

## Dictionary comprehension
grades = {
    "Alice": 85,
    "Bob": 72,
    "Carlos": 91,
    "Diana": 64
}

curved_grades = {name: score + 5 for name, score in grades.items()}

print(curved_grades)

# keep only passing students
passing_grades = {name: score for name, score in grades.items() if score >= 70}

print(passing_grades)

## Working with Strings
words = ["apple", "banana", "cherry", "date"]

lengths = [len(word) for word in words]

print(lengths)

# uppercase all words
upper_words = [word.upper() for word in words]

print(upper_words)

# keep words longer than 5 letters:
long_words = [word for word in words if len(word) > 5]

print(long_words)

# split strings into useful data
data = [
    "Alice,85",
    "Bob,72",
    "Carlos,91",
    "Diana,64"
]

records = [line.split(",") for line in data]

print(records)

# convert scores to integers
records = [(name, int(score)) for name, score in 
           [line.split(",") for line in data]]

print(records)

## nested list comprehensions
pairs = [(x, y) for x in [1, 2, 3] for y in [10, 20]]

print(pairs)

# equivalent to 
pairs = []

for x in [1, 2, 3]:
    for y in [10, 20]:
        pairs.append((x, y))

print(pairs)

## flattening a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = [number for row in matrix for number in row]

print(flat)

## List comprehension with if and else
scores = [85, 72, 91, 64]

labels = ["pass" if score >= 70 else "fail" for score in scores]

print(labels)

# filtering items
passing_scores = [score for score in scores if score >= 70]

# chosing between 2 values
labels = ["pass" if score >= 70 else "fail" for score in scores]


##