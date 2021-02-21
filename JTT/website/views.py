from flask import Blueprint, render_template, request, redirect, flash, jsonify
import json

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/port')
def port():
    return redirect('http://port.webapp:5000/')

@views.route('/about')
def about():
    return redirect('http://port.webapp:5000/about', code='302')


#@views.route('/about')
#def about():
#    return render_template("sobre.html")
