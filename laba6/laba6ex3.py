class Task:
    def __init__(self, date_start, date_finish, description):
        self.date_start = date_start
        self.date_finish = date_finish
        self.description = description
tasks = [
    Task("8:30", "9:30", "Занятие 1"),
    Task("9:40", "10:40", "Занятие 2"),
    Task("10:50", "11:50", "Занятие 3"),
    Task("12:00", "13:00", "Занятие 4"),
    Task("13:10", "14:10", "Занятие 5")
]
latest_task = max(tasks, date_finish)

output_message = (
    f"*Занятие, заканчивающееся позже всех:*\n"
    f"Дата начала: {latest_task.date_start}\n"
    f"Дата окончания: {latest_task.date_finish}\n"
    f"Описание: {latest_task.description}"
)

print(output_message)
