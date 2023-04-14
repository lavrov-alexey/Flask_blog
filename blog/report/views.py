from flask import Blueprint

report = Blueprint('report', __name__, url_prefix='/reports', static_folder='../static')


@report.route('/')
def report_list():
    return 'Hello report'
