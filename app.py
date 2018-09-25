from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/second")
def second_pr():
    return render_template('prs/second.html')


if __name__ == "__main__":
    app.run()
