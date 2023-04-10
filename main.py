# save this as app.py
from flask import Flask, jsonify, request
from users_controller import get_all_users, get_user_by_id

app = Flask(__name__)

@app.route("/api/users")
def users():
  return jsonify(get_all_users())

@app.route("/api/user/<id>")
def user(id):
  return jsonify(get_user_by_id(id))

@app.errorhandler(404)
def page_not_found(error):
  return {"error": "This page does not exist"}, 404

# Init the server
if __name__ == "__main__":
  app.run(host="127.0.0.1", port=3000, debug=True)