def mark_completed(tasks, task_name):
    if task_name in tasks:
        tasks[tasks.index(task_name)] += " (Completed)"
    return tasks

# Example usage:
tasks = ["Task 1", "Task 2", "Task 3"]
task_completed = "Task 2"
tasks = mark_completed(tasks, task_completed)
print("Tasks after marking as completed:", tasks)
