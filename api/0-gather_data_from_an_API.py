#!/usr/bin/python3
"""Returns TODO list progress for a given employee ID"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos").json()

    done_tasks = [task for task in todos if task["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))

    for task in done_tasks:
        print("\t{}".format(task.get("title")))
