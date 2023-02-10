# 0. Create a dictionary called `students` from 'favorite_colors.dat'
students = {}
f = open("favorite_colors.dat")
f.readline()  # discard the header line
for line in f:
    line = line.strip()
    fields = line.split()
    students[fields[0]] = fields[1]
f.close()

# 1. Print the number of pairs in the dictionary `students`
print(f"There are {len(students)} students in this dictionary")


# 2. Print the dictionary `students` all at once
print(students)


# 3. Print pairs one-by-one, by key
for student in students:
    print(f"  {student} likes {students[student]}")


# 4. Print only certain keys
print(f"Ammon likes the color {students['Ammon']}")
print(f"Edie likes the color {students['Edie']}")
print(f"Peter likes the color {students['Peter']}")


# 5. Safely check whether a key exists
if 'Daniela' in students:
    print(f"Daniela likes the color {students['Daniela']}")
else:
    print(f"You know what? I don't actually know what color Daniela likes")


# 6. Safely retrieve a value from `students`, getting a default otherwise
print(f"Erik's favorite color is {students.get('Erik', 'Beige')}")


# 7. Reverse the mapping:
#    Create a dictionary called `colors` associating colors to students who like it
colors = {}
for student in students:
    if students[student] in colors:
        colors[students[student]].append(student)
    else:
        colors[students[student]] = [ student ]
print(f"There are {len(colors)} colors in this dictionary")

for color in colors:
    print(f"  {color} is liked by {colors[color]}")
