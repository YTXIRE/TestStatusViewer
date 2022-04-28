from pkg.db.db import save_log, get_log


def save_logs(data):
    return save_log(data=data)


def get_logs(project):
    return get_log(project=project)
