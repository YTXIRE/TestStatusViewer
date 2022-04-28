    from flask import Flask, request
from internal.services.logs import save_logs, get_logs
from internal.services.projects import get_projects
from internal.services.db import create_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return {"hello": "niggga"}


@app.route("/create_db")
def action_create_db():
    try:
        create_db()
        return {"message": "OK"}, 200
    except BaseException as ex:
        return {'message': ex}, 500


@app.route("/set_logs", methods=["POST"])
def action_set_logs():
    try:
        data = request.get_json()
        save_logs(data=data)
        return {"message": "OK"}, 200
    except BaseException as ex:
        return {'message': ex}, 500


@app.route("/get_logs", methods=["GET"])
def action_get_logs():
    try:
        project = request.args.get('project')
        period = request.args.get('period')
        return {"data": get_logs(project=project)}, 200
    except BaseException as ex:
        return {'message': ex}, 500


@app.route("/get_projects", methods=["GET"])
def action_get_projects():
    try:
        return {"data": get_projects()}, 200
    except BaseException as ex:
        return {'message': ex}, 500
