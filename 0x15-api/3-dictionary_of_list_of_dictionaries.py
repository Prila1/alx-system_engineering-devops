#!/usr/bin/python3
"""Gathers data from an api and stores them in a JSON file."""

import json
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'
JSON_FILE = 'todo_all_employees.json'


obj = {}
employees = requests.get('{}/users'.format(BASE_URL)).json()
for employee in employees:
    all_tasks = requests.get('{}/todos?userId={}'.format(
        BASE_URL, employee.get('id'))).json()
    obj[employee.get('id')] = [
            {
                'username': employee.get('username'),
                'task': t.get('title'),
                'completed': t.get('completed'),
            } for t in all_tasks
    ]

with open(JSON_FILE, 'w', encoding='utf-8') as j_f:
    j_writer = json.dump(obj, j_f)
