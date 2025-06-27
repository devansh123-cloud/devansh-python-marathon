#task store
tasks = []
#count
count = int(input("How many task? "))
#range
for i in range(1, count+1):
    task = input(f"Enter a task {i} :")
    tasks.append(task)
#print
print("\nYour To-Do List:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")