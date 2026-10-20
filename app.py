from flask import Flask
from flask import render_template
import markdown 
from markdown.extensions.toc import TocExtension
import os

app = Flask(__name__) #name of application package 

@app.route("/") #index
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    projects = os.listdir("projects")
    print(projects)
    return render_template("projects.html")

@app.route("/projects/#")
def project_view():
    return 

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/projects/in-progress")
def in_progress():
    return render_template("in-progress.html")

@app.route("/blog")
def blog():
    return render_template("blog.md")

#python code to read the markdown files

'''
for each file in the folder, 
convert to html with python-markdown
add a div of class "content" to the page (either blog or projects) with the html inside. 
'''
