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
    try:
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
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred during calculation"}), 500


@app.route("/echo", methods=["POST"])
def echo():
    posted = request.get_json()
    posted["echoed"] = True
    return jsonify(posted)

@app.route("/status/<int:code>")
def status(code):
    message = f"This is a {code} error"
    return message


@app.before_request
def before_request():
    print(request, request.path)

@app.after_request
def after_request(response):
    response.headers['X-Custom-Header'] = 'FlaskRocks'
    return response

@app.teardown_request
def teardown_request(exception):
    print(exception)


@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)

if __name__ == '__main__':
    app.run(debug=True, port=5000)