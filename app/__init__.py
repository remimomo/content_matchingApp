from flask import Flask

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flash messages

from app import routes
