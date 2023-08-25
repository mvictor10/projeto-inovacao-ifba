from flask import Flask, render_template, Response, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
	"mvictor": "65564747"
}

@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')


@auth.verify_password
def verify_password(username, password):
    if username in users and password == users.get(username):
        return username


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000, debug=True)