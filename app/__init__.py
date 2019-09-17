from flask import Flask
print("Initializing Flask")

app = Flask(__name__)

from app import routes
print("Initializing Routes")