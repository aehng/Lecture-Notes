from Beatles import george, john, paul, ringo
import Presidents
# Change this line for question #5


print("The code in main.py is in the namespace", __name__)
print()

# Change this line for question #6

print("Presenting the Beatles!")
print(george())
print(john())
print(paul())
print(ringo())
print()


print("Presenting the Presidents of the United States of America!")
print("  ...no, not the band from the 90's...")
print(Presidents.george())
print(Presidents.john())
print(Presidents.thomas())
print(Presidents.james())
print()


# This statement doesn't work
# Add a new import statement that fixes this line of code 
print(Beatles.george())
