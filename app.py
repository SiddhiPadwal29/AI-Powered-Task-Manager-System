from flask import Flask
from routes.auth_routes import auth
from routes.task_routes import task

app = Flask(__name__)

app.secret_key = "secretkey"

app.register_blueprint(auth)
app.register_blueprint(task)

if __name__ == '__main__':
    app.run(debug=True)
