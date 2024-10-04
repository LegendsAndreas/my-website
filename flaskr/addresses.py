from flask import Blueprint, render_template
from os import walk

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    # You can also send variables, that can be used in that html files. You just access them by writing: {{ [VARIABLE_NAME] }}
    return render_template('home.html', test="Andreas")

@bp.route("/cat-home")
def cat():
    # "cats", holds all the images of the cats in the folder "pics" and sends them to "cat_home.html"
    # The variables "cats" in render_template, has to be the same as the variable in your Jinja2 code.
    cats_array = []
    for (dirpath, dirnames, filenames) in walk("resources\pics"):
        cats_array.extend(filenames)
        break

    return render_template("cat_home.html", cats=cats_array)

@bp.route("/code-home")
def code():
    return render_template("code_home.html")

@bp.route("/merle")
def merle():
    return render_template("cat_merle.html")

@bp.route("/fie")
def fie():
    return render_template("cat_fie.html")