#!/usr/bin/python3
""" for a given employee ID, returns information about their TODO list """
import requests
import json
import sys

def to_do(emp_id=int(sys.argv[1])):
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users_list = json.loads(users.text)
    todos_list = json.loads(todos.text)
    for user in users_list:
        if user['id'] == emp_id:
            completed_tasks = 0
            total_tasks = 0
            username = 'John'
            comp_list = []
            for task in todos_list:
                if task['userId'] == user['id']:
                    if task['completed'] == True:
                        comp_list.append(task['title'])
                        completed_tasks += 1
                    total_tasks += 1
                    username = user['name']
            str1 = f"Employee {username} is done with "
            str2 = f"tasks({completed_tasks}/{total_tasks})"
            print(str1 + str2)
            for element in comp_list:
                print('  ' + element)
            break
to_do()
