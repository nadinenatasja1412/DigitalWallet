from flask import Flask

app = Flask(__name__)

@app.route ('/')
def homel():
    return "Hello from Flask !"

if __name__ == '_main_':
    app.run(debug=True)