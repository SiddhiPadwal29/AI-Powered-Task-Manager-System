from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/api/tasks')
def get_tasks():
    return jsonify({
        "task": "Complete DevOps Project",
        "status": "Pending"
    })
