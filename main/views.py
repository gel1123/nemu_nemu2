from flask import Flask, render_template, request, redirect
from main import app
from main.models import Entry
from main import db
import json

@app.route('/')
def show_entries():
    return render_template("test3.html", title="jstool")
