#!/usr/bin/python3
""" Using what you did in the task #0, extend your
Python script to export data in the CSV format. """
import csv
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
    filename = "{}.csv".format(user_id)
    for task in total_tasks:
        c_tasks.append((user_id, username, task.get("completed"),
                        task.get("title")))

    with open(filename, "w") as f:
        file_w = csv.writer(f, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for task in c_tasks:
            file_w.writerow(task)
