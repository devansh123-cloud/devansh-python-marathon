# How many tasks? 3
# Enter task 1: Buy milk
# Enter task 2: Study Python
# Enter task 3: Go for a walk

# Your To-Do List:
# - Buy milk
# - Study Python
# - Go for a walk

tasks = []
count = int(input("How many task? "))

for i in range(1, count+1):
    task = input(f"Enter a task {i} :")
    tasks.append(task)
    
print("\nYour To-Do List:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")