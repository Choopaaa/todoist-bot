from http.client import InvalidURL
from json import JSONDecodeError
from logging import exception
import requests


headers = {"Authorization": "Bearer 839f660cc572bd387ef85163b740e334d1fa768a"}

# Получение списка задач
def get_tasks():

    try:
        response = requests.get('https://api.todoist.com/rest/v1/tasks', headers = headers)
        response_json = response.json()

        return response_json

    except InvalidURL:
        print("Введён неверный адрес сайта")
    except JSONDecodeError as error:
        print(error)
        
# Добавление новой задачи
def add_tasks(message):
    
    try:
        response1 = requests.post(
            'https://api.todoist.com/rest/v1/tasks', 
            data = {'content': message}, 
            headers = headers
        )
        response1_json = response1.json()

        if response1.status_code == 200:
            print(True)

        return response1_json
    except InvalidURL:
        print("Введён неверный адрес сайта")
    except JSONDecodeError as error:
        print(error)

# Удаление задачи
def delete_tasks(task_id):

    try:

        response2 = requests.delete(f'https://api.todoist.com/rest/v1/tasks/{task_id}', headers = headers)
        response2_json = response2.json()

        if response2.status_code == 204:
            print(True)

        return response2_json

    except InvalidURL:
        print("Введён неверный адрес сайта")
    except JSONDecodeError as error:
        print(error)

add_tasks("Я задача")