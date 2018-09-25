from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/first")
def first_pr():
    return render_template('prs/first.html')


if __name__ == "__main__":
    app.run()
