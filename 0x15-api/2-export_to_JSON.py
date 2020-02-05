#!/usr/bin/python3
"""  Python script to export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = '{}users/{}'.format(url, user_id)
    reqname = requests.get(user).json()
    todos = '{}todos?userId={}'.format(url, user_id)
    total_tasks = requests.get(todos).json()
    username = reqname.get("username")
    c_tasks = []
    filename = "{}.json".format(user_id)

    for task in total_tasks:
        dict_users = {"task": task.get("title"),
                      "completed": task.get("completed"),
                      "username": username}
        c_tasks.append(dict_users)
    user_dict = {user_id: c_tasks}

    with open(filename, 'w') as f:
        json.dump(user_dict, f)
