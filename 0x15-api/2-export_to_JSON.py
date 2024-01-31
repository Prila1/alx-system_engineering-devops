#!/usr/bin/python3

"""
Gathers data from an api and displays them in stdout.
"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    JSON_FILE = '{}.json'.format(employee_id)

    employee = requests.get('{}/users/{}'.format(BASE_URL, employee_id)).json()
    all_tasks = requests.get(
        '{}/users/{}/todos'.format(BASE_URL, employee_id)).json()

    with open(JSON_FILE, 'w', encoding='utf-8') as j_f:
        obj = {
            employee.get('id'): [
                {
                    'task': t.get('title'),
                    'completed': t.get('completed'),
                    'username': employee.get('username')
                }for t in all_tasks]
        }
        j_writer = json.dump(obj, j_f)
