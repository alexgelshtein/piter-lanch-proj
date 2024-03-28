import os
from dotenv import load_dotenv
from flask import Flask

from lanch import pages

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    
    app.register_blueprint(pages.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app