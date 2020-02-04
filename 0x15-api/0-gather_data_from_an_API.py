#!/usr/bin/python3
""" Python script that, using this REST API: jsonplaceholder
returns information about his/her TODO list progress. """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    rnid = requests.get(user).json()
    name = rnid.get('name')

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    total_tasks = requests.get(todos).json()

    done_tasks = []
    for elem in total_tasks:
        if elem.get("completed") is True:
            done_tasks.append(elem)

    print("Employee {} is done with tasks({}/{})"
          .format(name, len(done_tasks), len(total_tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
