import sqlite3
from datetime import datetime
from math import ceil


def connect():
    sqlite_connection = sqlite3.connect('../db/db.db')
    cursor = sqlite_connection.cursor()
    return cursor, sqlite_connection


def create():
    cursor, connection = connect()
    f = open('../init.sql', 'r')
    sql = f.read()
    cursor.executescript(sql)

def save_log(data):
    try:
        cursor, connection = connect()
        data['message'] = str(data['message']).replace("'", "\\'").replace('"', "'")
        sql = f"""INSERT INTO reports (message, status, test_name, created_at, project) VALUES ("{data['message']}", "{data['status']}", "{data['test_name']}", {ceil(datetime.now().timestamp())}, "{data['project']}")"""
        count = cursor.execute(sql)
        connection.commit()
        return "OK"
    except BaseException as ex:
        print(ex)


def get_log(project):
    try:
        cursor, connection = connect()
        sql = f"""SELECT * FROM reports WHERE project = "{project}" AND created_at > "{datetime.now().timestamp() - 60 * 60}" ORDER BY id desc"""
        cursor.execute(sql)
        records = []
        for record in cursor.fetchall():
            records.append({
                'id': record[0],
                'message': record[1].replace("\\'", "'"),
                'status': record[2],
                'test_name': record[3],
                'created_at': record[4],
                'project': record[5],
            })
        return records
    except BaseException as ex:
        print(ex)


def get_project():
    try:
        cursor, connection = connect()
        sql = f"""SELECT * FROM projects"""
        cursor.execute(sql)
        projects = []
        for project in cursor.fetchall():
            projects.append(project[0])
        return projects
    except BaseException as ex:
        print(ex)
