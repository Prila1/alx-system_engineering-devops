#!/usr/bin/python3

"""
Gathers data from an api and displays them in stdout.
"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    CSV_FILE = '{}.csv'.format(employee_id)

    employee = requests.get('{}/users/{}'.format(BASE_URL, employee_id)).json()
    all_tasks = requests.get(
        '{}/users/{}/todos'.format(BASE_URL, employee_id)).json()

    with open(CSV_FILE, 'w', encoding='utf-8') as c_f:
        c_writer = csv.writer(c_f, dialect='unix')
        c_writer.writerows([
            [employee.get('id'),
                employee.get('username'),
                t.get('completed'),
                t.get('title')] for t in all_tasks])
