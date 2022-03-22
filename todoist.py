from todoist_api_python.api import TodoistAPI

api = TodoistAPI('839f660cc572bd387ef85163b740e334d1fa768a')

# Показать список задач : 
def show_task():
    try:
        tasks = api.get_tasks()
        print(tasks)
    except Exception as error:
        print(error)

# Добавить новую задачу :
def add_task():
    try:
        task = api.add_task(
            content='Buy Milk',
            due_string='tomorrow at 12:00',
            due_lang='en',
            priority=4,
        )
        print(task)
    except Exception as error:
        print(error)

# Удалить задачу: 
def del_task():
    try:
        is_success = api.delete_task(task_id=2995104339)
        print(is_success)
    except Exception as error:
        print(error)