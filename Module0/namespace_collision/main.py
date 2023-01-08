from Beatles import paul, george, ringo
import Presidents


print(f"The code in main.py is in the namespace {__name__}")
print(george())
print(Presidents.george())

# This won't work with the import statement 'from Beatles import paul, george, ringo'
# I'll need to 'import Beatles' to do this
print(Beatles.george())
