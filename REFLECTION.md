The app.route decorator determines the url that will trigger the function below it to run.
Flask knows which function to call when a request arrives based on the @app.route annotaion.
Route parameters are written as part of the url path and are drawn out by passing the value into the function.
Query parameters are added on after a ? placed at the end of the url path, the parameter is written with its value and
drawn out using request.args.get(parameter name).
For POST requests we are extracting the json that is returned. For GET requests we are extracting the values that were sent
with the request.
If you try to access request.args outside of a function it will return an error.

Thank you!