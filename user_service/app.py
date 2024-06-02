from flask import Flask
from error_handlers import register_error_handlers

app = Flask(__name__)

register_error_handlers(app)

