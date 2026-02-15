from flask import Flask, request, current_app, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(request)
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    print(request)
    return jsonify({"name": "Bracha Glazer", "course": "MCON-504 - Backend Development", "semester": "Spring 2026"})

@app.route("/greet/<name>")
def greet(name):
    print(request)
    return f"<p>Hello, {name}! Welcome to Flask.</p>"

@app.route("/calculate")
def calculate():
    print(request)
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    operation = request.args.get('operation')
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "mul":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    else:
        result = None
    return jsonify({"result": result, "operation": operation})

@app.route("/echo", methods=["POST"])
def echo():
    posted = request.get_json()
    posted["echoed"] = True
    return jsonify(posted)

@app.route("/status/<int:code>")
def status(code):
    message = f"This is a {code} error"
    return message

if __name__ == '__main__':
    app.run(debug=True, port=5000)