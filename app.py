from flask import Flask, render_template, url_for

app = Flask(__name__)

all_posts = [
    {
            'title': 'Post1',
            'content': 'Content of post 1'
    },

    {
            'title': 'Post2',
            'content': 'Content of post 2'
    }
]

@app.route("/posts")
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
