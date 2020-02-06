#!/usr/bin/python3
""" Python script to export data in the JSON format."""
import json
import requests


import json
import requests


if __name__ == "__main__":
    """ Main method """
    url = "https://jsonplaceholder.typicode.com/"
    users_dict = requests.get('{}users/'.format(url)).json()
    user_task = {}
    for user in users_dict:
        user_name = user.get('username')
        user_id = user.get('id')
        todos = '{}todos?userId={}'.format(url, user_id)
        total_dict = requests.get(todos).json()
        c_tasks = []
        for task in total_dict:
            dict_task = {"username": user_name,
                         "task": task.get("title"),
                         "completed": task.get("completed")}
            c_tasks.append(dict_task)

            user_task[str(user_id)] = c_tasks
            filename = "todo_all_employees.json"
            with open(filename, mode='w') as f:
                json.dump(user_task, f)
