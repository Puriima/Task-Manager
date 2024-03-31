class Task:
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        return f"{self.description} by {self.deadline} - {'Done' if self.status else 'Not Done'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append(Task(description, deadline))

    def mark_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                break

    def show_tasks(self):
        for task in self.tasks:
            if not task.status:
                print(task)


# Использование
tm = TaskManager()
tm.add_task("Complete Python project", "2023-04-15")
tm.add_task("Write a blog post", "2023-04-20")
tm.show_tasks()

tm.mark_done("Complete Python project")
tm.show_tasks()