from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@Vamsi_2008_vamsi'


if __name__ == "__main__":
    app.run()
