from turtle import pos
from flask import Flask, render_template
import requests

app = Flask(__name__)

postEndPoint = "https://api.npoint.io/f476d79b9a09cf7b9097"
res = requests.get(url=postEndPoint)
allPosts = res.json()

@app.route("/")
def home():
    return render_template("index.html", posts=allPosts)


@app.route("/post/<int:id>")
def blog_post(id):
    myPost = None
    for post in allPosts:
        if post["id"] == id:
            myPost = post
    return render_template("post.html", post=myPost)

if __name__ == "__main__":
    app.run(debug=True)