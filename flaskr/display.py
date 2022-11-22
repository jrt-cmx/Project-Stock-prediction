import datetime
import time
from flask import Blueprint, request, render_template
from flaskr.models import  Search
from .finance import CompanyStock


display = Blueprint('display', __name__)


@display.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    return displayHome()
  
  search = Search(time=time.time(), search_term= search_symbol)
  return displayStock(search_symbol)


def displayHome(**kwargs):
  return render_template('home.html')


def displayStock(symbol):
  search_error = 'Error: Stock symbol does not exist'
  company = CompanyStock(symbol)

  if company.get_symbol() is None:
        return displayHome(search_error=search_error)
  
  return render_template(
        'stock.html',
        company_symbol=company.get_symbol(),
        company=company.get_info('longName'),
    )


def search ():
  # Get search symbol
  search_symbol = request.form.get('search_symbol')
    

  return displayStock(search_symbol)


