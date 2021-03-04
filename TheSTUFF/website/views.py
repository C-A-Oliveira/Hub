from flask import Blueprint, render_template, render_template_string, request, flash, jsonify, session
import json
from Stuffy import mailer, mapper

import urllib.request	

git_raw = ['https://raw.githubusercontent.com/C-A-Oliveira/{repo}/{file}',
            'https://raw.githubusercontent.com/C-A-Oliveira/{path}']

## Reads the raw code of a given repo from the author of the project... AKA me

def get_file_from(repo, file):
    request = urllib.request.urlopen(git_raw[0].format(repo = repo, file = file))
    return request.read().decode("utf8")

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template("cover.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/projects')
def projects():
    return wip()
    #return render_template("projects.html")

@views.route('/sandbox' , methods=["GET", "POST"])
def sandbox():    
    # The POST/GET request needs to tell:
    # > what the language of code is    -       ()
    # > what project itself is ...      -       ()
    # > what are the args to be used    -       (DONE)
    # After that that informations is sent to de <mapper> so it can decide where it goes.
    # If I did that here on the 'views' this shit would be impossibly tedeous and difficult
    # to debug... Don't @ me
    ## Maybe i could call the damn method/funtion/code dictly... IDNC F-it 
    #return wip()
    if request.method == "POST":
        #print(request.form.to_dict())
        #post_list = list(request.form.to_dict().values())
        
        post_list = list(request.get_json(force=True).values())
        print(post_list)
        return mapper.do_shit(post_list)
    else:
        return render_template("sandbox.html")

@views.route('/sandbox/getSource' , methods=["POST"])
def getSource():    
    # The POST/GET request needs to tell:
    # > what the language of code is    -       ()
    # > what project itself is ...      -       ()
    # > what are the args to be used    -       (DONE)
    # After that that informations is sent to de <mapper> so it can decide where it goes.
    # If I did that here on the 'views' this shit would be impossibly tedeous and difficult
    # to debug... Don't @ me
    ## Maybe i could call the damn method/funtion/code dictly... IDNC F-it 
    #return wip()
    return get_file_from('Hub/master/TheSTUFF/Stuffy/displayProjects/py', 'randPassGen.py')

@views.route('/about')
def about():
    return render_template("about-cesar.html")

@views.route('/contact' , methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        company = request.form["company"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        print(f"> new e-mail request from {name} @ {email}")
        mailer.send_it(name, email)

        # add the person a list of some sort...
        # add_to_reply(name, company, email, subject, message)
    return render_template("contact.html")

@views.route('/wip')
def wip():
    return render_template("wip.html")

@views.route('/test/<num>' , methods=["GET", "POST"])
def test(num):
    if request.method == "POST":
        print(request.get_json(force=True))
    return render_template(f"test-{num}.html")
