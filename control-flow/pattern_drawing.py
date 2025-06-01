# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Start from row 0
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print each * in the row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1
