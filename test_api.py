from flask import Flask, request, current_app, jsonify
import requests

response = requests.get('http://localhost:5000/')
print(f"Status Code: {response.status_code}")
print(f"Content: {response.headers.get("Content-Type")}")

response = requests.get('http://localhost:5000/about')
print(f"Status Code: {response.status_code}")
print(response)

response = requests.get('http://localhost:5000/greet/Bracha')
print(f"Status Code: {response.status_code}")
print(response)

response = requests.get('http://localhost:5000/calculate?num1=4&num2=6&operation=add')
print(f"Status Code: {response.status_code}")
print(response)

response = requests.get('http://localhost:5000/calculate?num1=10&num2=7&operation=sub')
print(f"Status Code: {response.status_code}")
print(response)

response = requests.get('http://localhost:5000/calculate?num1=4&num0=6&operation=div')
print(f"Status Code: {response.status_code}")
print(response)

response = requests.get('http://localhost:5000/echo')
requests.body= {'testing': 4}
print(f"Status Code: {response.status_code}")
print(response)

response = requests.get('http://localhost:5000/status/400')
print(f"Status Code: {response.status_code}")
print("400", response)

response = requests.get('http://localhost:5000/status/500')
print(f"Status Code: {response.status_code}")
print("500", response)

response = requests.get('http://localhost:5000/')
custom_header = response.headers.get('X-Custom-Header')
print(f"Status Code: {response.status_code}")
print(f"Custom Header: {custom_header}")

response = requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=div')
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")