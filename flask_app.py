from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "well done the flask application is running successfully using jenkins + docker + aws ec2 instance"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
