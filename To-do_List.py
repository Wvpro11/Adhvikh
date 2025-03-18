print("Welcome to To-Do List")

# Open the file in append mode to store tasks
with open("tasks.txt", "a") as file:
    while True:
        task = input("Type your task (or type 'no' to stop adding): ")
        if task.lower() == "no":
            break
        file.write(task + "\n")  # Write task to file

# Ask if the user wants to see stored tasks
output = input("Do you want to see your tasks? (yes/no): ").lower()
if output == "yes":
    print("\nYour To-Do List:")
    with open("tasks.txt", "r") as file:
        print(file.read())  # Read and display tasks
else:
    print("Okay, have a great day!")
