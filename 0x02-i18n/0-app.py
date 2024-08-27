#!/usr/bin/env python3
"""
0-app.py
"""

from flask import Flask, render_template
from typing import Any


app = Flask(__name__)


@app.route('/')
def index() -> Any:
    """
    renders the index template
    """
    return render_template('0-index.html')
