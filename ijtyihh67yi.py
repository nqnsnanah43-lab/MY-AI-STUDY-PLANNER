
# Beginner-Friendly AI Study Planner

print("===================================")
print("     MY AI STUDY PLANNER")
print("===================================")

# Get student information
name = input("Enter your name: ").strip()

while not name:
    name = input("Name cannot be empty. Enter your name: ").strip()

goals = input("What are your AI learning goals? ").strip()

while not goals:
    goals = input("Please enter your AI learning goals: ").strip()

# Get study days
while True:
    try:
        days = int(input("How many days per week will you study (1-7)? "))
        if 1 <= days <= 7:
            break
        print("Please enter a number from 1 to 7.")
    except ValueError:
        print("Please enter a whole number.")

# Get daily study hours
while True:
    try:
        hours = float(input("How many hours will you study each day? "))
        if 0 < hours <= 24:
            break
        print("Enter a number greater than 0 and at most 24.")
    except ValueError:
        print("Please enter a valid number.")

# Calculate weekly study hours
weekly_hours = days * hours

# Create a personalized study plan
plan = f"""
===================================
       MY AI STUDY PLAN
===================================

Student Name: {name}

AI Learning Goals:
{goals}

Study Days Per Week: {days}
Daily Study Hours: {hours:g}
Total Weekly Study Hours: {weekly_hours:g}

PERSONALIZED STUDY SCHEDULE
-----------------------------------

Day 1: Learn AI basics and key concepts.
Day 2: Study Python fundamentals.
Day 3: Explore data and simple examples.
Day 4: Practice with small Python exercises.
Day 5: Learn basic machine learning concepts.
Day 6: Work on a mini project related to your goals.
Day 7: Review your learning or take a rest day.

Study on your chosen {days} day(s) each week.
Choose the schedule activities that best match
your goals: {goals}

PERSONALIZED STUDY ADVICE
-----------------------------------
"""

if weekly_hours < 3:
    plan += (
        "Start slowly. Focus on short lessons and "
        "consistent practice.\n"
    )
elif weekly_hours < 7:
    plan += (
        "Build a steady routine. Combine learning "
        "with hands-on Python exercises.\n"
    )
elif weekly_hours < 14:
    plan += (
        "You have time for regular practice and "
        "a small project each week.\n"
    )
else:
    plan += (
        "Create a balanced schedule with breaks, "
        "practical projects, and regular revision.\n"
    )

plan += """
Remember: Consistency is more important than speed.
Keep learning one step at a time!

===================================
"""

# Display the study plan
print(plan)

# Save the study plan to a text file
try:
    with open("study-plan.txt", "w", encoding="utf-8") as file:
        file.write(plan)

    print("Your study plan was saved to study-plan.txt.")

except OSError:
    print("Unable to save the file. Check folder permissions.")
