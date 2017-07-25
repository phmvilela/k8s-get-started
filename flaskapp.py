from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '{"message" : "This is a k8s get started test. V5"}', 200, {"Content-Type" : "application/json"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
