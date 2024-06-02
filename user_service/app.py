from flask import Flask
from error_handlers import register_error_handlers

app = Flask(__name__)

# Register error handling middleware
register_error_handlers(app)

# Other app configurations and route definitions...
