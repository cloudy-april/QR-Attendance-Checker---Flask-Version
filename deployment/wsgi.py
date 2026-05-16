"""WSGI entry point for Azure App Service."""

import os
import sys


CURRENT_DIR = os.path.dirname(__file__)
APP_SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "app", "src"))

if APP_SRC_DIR not in sys.path:
    sys.path.insert(0, APP_SRC_DIR)

from flask_app import create_app


app = create_app()
application = app
