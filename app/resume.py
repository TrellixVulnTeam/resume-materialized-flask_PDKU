from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def render_resume():
    return render_template('index.html')


@app.route("/testing")
def render_testing():
    return render_template('testing.html')


@app.route('/index-test')
def render_hometest():
    return render_template('index_testing.html')


if __name__ == "__main__":
    app.run()
