from flask import Flask, render_template

app = Flask(__name__)


# Routes
@app.route('/')
def root():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
