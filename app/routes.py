from flask import (
    Flask,
    render_template
)

import requests

BACKEND_URL = "http://127.0.0.1:5000"


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")

@app.get("/about")
def about():
    out = {
        "up": False
    }
    ping_url = "%s/%s" % (BACKEND_URL, "ping")
    up = requests.get(ping_url)
    if up.status_code == 200:
        out["up"] = True
        version_url = "%s/%s" % (BACKEND_URL, "version")
        version_response = requests.get(version_url)
        version_json = version_response.json()
        out["version"] = version_json.get("version")
    return render_template("about.html", content=out)


@app.get("/users")
def display_users():
    user_url = "%s/%s" % (BACKEND_URL, "users")
    response = requests.get(user_url)
    if response.status_code == 200:
        response_json = response.json()
        user_list = response_json.get("users")
        return render_template("user_list.html", users=user_list)
    else:
        return render_template("error.html")
