#!/usr/bin/python3
""" For a given employee ID, returns information about their TODO list """
import csv
import json
import requests
import sys


def to_do(emp_id=0):
    if len(sys.argv) == 1:
        return
    emp_id = int(sys.argv[1])
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users_list = json.loads(users.text)
    todos_list = json.loads(todos.text)
    user_tasks = []
    for user in users_list:
        if user['id'] == emp_id:
            completed_tasks = 0
            total_tasks = 0
            username = 'John'
            comp_list = []
            for task in todos_list:
                if task['userId'] == user['id']:
                    user_tasks.append(task)
                    if task['completed'] is True:
                        comp_list.append(task['title'])
                        completed_tasks += 1
                    total_tasks += 1
                    name = user['name']
                    username = user['username']
            str1 = "Employee " + str(name) + " is done with "
            s = "tasks(" + str(completed_tasks) + "/" + str(total_tasks) + "):"
            print(str1 + s)
            for element in comp_list:
                print('\t ' + element)
            break
    csvfile = str(emp_id) + ".csv"
    with open(csvfile, 'w') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            wr.writerow([emp_id, username, task['completed'], task['title']])
    json_list = []
    task_dict = {}
    for task in user_tasks:
        task_dict["task"] = task['title']
        task_dict["completed"] = task['completed']
        task_dict["username"] = username
        json_list.append(task_dict)
    json_dict = {str(emp_id) : json_list}
    jsonfile = str(emp_id) + ".json"
    with open(jsonfile, 'w') as f2:
        wr2 = json.dump(json_dict, f2)

if __name__ == "__main__":
    to_do()
