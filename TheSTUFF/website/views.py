from flask import Blueprint, render_template, request, flash, jsonify
import json

views = Blueprint('views', __name__)


@views.route('/')
def landing():
    return render_template("cover.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about-cesar.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/wip')
def wip():
    return render_template("wip.html")

@views.route('/projects')
def projects():
    return wip()
    #return render_template("projects.html")

