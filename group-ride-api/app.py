from flask import Flask, jsonify, request
app = Flask(__name__)


posts = [

]

@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/posts")
def get_posts():
  return jsonify(posts)


@app.route("/posts", methods=["POST"])
def add_post():
  posts.append(request.get_json())
  return '', 204