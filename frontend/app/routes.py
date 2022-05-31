from cmath import log
from flask import (
  Flask,
  request,
  redirect,
  url_for,
  render_template
)

import requests
BACKEND_URL = "http://127.0.0.1:5000"

app = Flask(__name__)

@app.get("/")
def index():
  return render_template("index.html")

def get_user(pk):
  url = "%s/users/%s" % (BACKEND_URL, pk) # http://127.0.0.1:5000/users/1
  response = requests.get(url)
  my_response = response.json()
  return my_response

@app.get("/users/new")
def create_user():
  return render_template("new_user.html")

@app.post("/users/create")
def send_user_create_request():
  url = "%s/%s" % (BACKEND_URL, "users")
  form_data = request.form
  user_json = {
    "first_name": form_data.get("first_name"),
    "last_name": form_data.get("last_name"),
    "hobbies": form_data.get("hobbies"),
  }
  response = requests.post(url, json=user_json)
  if response.status_code == 204:
    return render_template("user_creation_success.html")
  else:
    return render_template("400.html"), 400

@app.get("/users")
def user_list():
  url = "%s/%s" % (BACKEND_URL, "users")
  response = requests.get(url)
  if response.status_code == 200:
    resp_json = response.json()
    users = resp_json.get("users")
    return render_template("user_list.html", user_list=users)
  else:
    return render_template("400.html"), 400

@app.get("/users/<int:pk>")
def delete_user(pk):
  URL= "http://127.0.0.1:5000/users"
  url = "%s/%s" % (URL,  pk) # http://127.0.0.1:5000/users/1
  response = requests.delete(url)
  if response.status_code == 204:
    return render_template('user_deleted_success.html')
  else:
    return render_template("400.html"), 400

@app.get("/users/update/<user_id>")
def testing(user_id):
  user = get_user(user_id)
  return render_template("update_user.html", user=user["user"][0]), 400

@app.post("/user/update/<pk>")
def update_user(pk):
  form_data = request.form
  url = "%s/users/%s" % (BACKEND_URL, pk)
  user_json = {
    "first_name": form_data.get("first_name"),
    "last_name": form_data.get("last_name"),
    "hobbies": form_data.get("hobbies"),
  }
  response = requests.put(url, json=user_json)
  if response.status_code == 204:
    return render_template("user_updated_success.html")
  else:
    return render_template("400.html"), 404

@app.get("/user/profile/<int:pk>")
def get_user_profile(pk):
  user = get_user(pk)
  return render_template("profile_view.html", user=user["user"][0])