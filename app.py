"""Synthetic analysis fixture. Never run or deploy this application."""

import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.get("/users")
def find_users():
    name = request.args["name"]
    connection = sqlite3.connect(":memory:")
    return str(connection.execute("SELECT * FROM users WHERE name = '" + name + "'").fetchall())


@app.get("/diagnostics")
def run_diagnostic():
    host = request.args["host"]
    return subprocess.check_output("ping -c 1 " + host, shell=True, text=True)

