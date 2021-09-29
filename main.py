from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Learning Heroku in Praxis"

@app.route('/someendpoits')
def firstendpoint():
    return "This is my first path on heroku"

if __name__ == "__main__":
    app.run()
