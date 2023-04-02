#!/usr/bin/python3
""" For a given employee ID, returns information about their TODO list """
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
    for user in users_list:
        if user['id'] == emp_id:
            completed_tasks = 0
            total_tasks = 0
            username = 'John'
            comp_list = []
            for task in todos_list:
                if task['userId'] == user['id']:
                    if task['completed'] is True:
                        comp_list.append(task['title'])
                        completed_tasks += 1
                    total_tasks += 1
                    username = user['name']
            str1 = "Employee " + str(username) + " is done with "
            s = "tasks(" + str(completed_tasks) + "/" + str(total_tasks) + "):"
            print(str1 + s)
            for element in comp_list:
                print('\t ' + element)
            break

if __name__ == "__main__":
    to_do()
