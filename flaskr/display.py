from flask import Blueprint, request, render_template


display = Blueprint('display', __name__)


@display.route("/")
def displayHome():
  return render_template('home.html')


def displayStock():
  return 'hi'

def search ():
  # Get search symbol
  search_symbol = request.form.get('search_symbol')
    

  return displayStock(search_symbol)
  