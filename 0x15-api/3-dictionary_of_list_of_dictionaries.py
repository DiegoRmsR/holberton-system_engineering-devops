#!/usr/bin/python3
""" Python script to export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/'.format(url)
    users_dict = requests.get(user).json()
    user_task = {}
    for user in users_dict:
        user_name = user.get('username')
        user_id = user.get('id')
        todos = "{}todos?userId={}".format(api_url, user_id))
        todo_dict = requests.get(todos).json()
        c_tasks = []
        for task in todo_dict:
            dict_task = {"username": user_name,
                         "task": task.get("title"),
                         "completed": task.get("completed")}
            c_tasks.append(dict_task)

            user_task[str(user_id)] = c_tasks
            filename = "todo_all_employees.json"
            with open(filename, 'w') as f:
                json.dump(user_task, f)
