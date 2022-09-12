from flask import Blueprint, request, render_template

display = Blueprint('display', __name__)


@display.route("/")
def home():
  return render_template('home.html')