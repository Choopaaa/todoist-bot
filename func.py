import requests


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

# Получение списка задач
def get_tasks():

    response = requests.get('https://api.todoist.com/rest/v1/tasks', auth=BearerAuth('839f660cc572bd387ef85163b740e334d1fa768a'))
    response_json = response.json()

    return response_json

# Добавление новой задачи
def add_tasks(message):
    
    response1 = requests.post(
        'https://api.todoist.com/rest/v1/tasks', 
        data = {'content': message}, 
        auth=BearerAuth('839f660cc572bd387ef85163b740e334d1fa768a')
    )
    response1_json = response1.json()
    
    return response1_json

# Удаление задачи
def delete_tasks(task_id):

    response2 = requests.delete(f'https://api.todoist.com/rest/v1/tasks/{task_id}', auth=BearerAuth('839f660cc572bd387ef85163b740e334d1fa768a'))
    response2_json = response2.json()

    return response2_json

print(get_tasks())
print(add_tasks())



