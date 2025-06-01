# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize message
message = f"Reminder: '{task}' is a {priority} priority task"

# Add time-sensitive note if applicable
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += "."

# Print final reminder
print()
print(message)

