from flask import Blueprint, render_template

task = Blueprint('task', __name__)

@task.route('/')
def dashboard():
    return render_template('dashboard.html')
