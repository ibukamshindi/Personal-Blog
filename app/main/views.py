from flask import render_template
from . import main
from ..request import get_quotes


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    myquote = get_quotes()
    quote = myquote['quote']
    quote_author = myquote['author']

    title = 'Home - Welcome to My Blog'
    return render_template('index.html', title = title, quote=quote,quote_author=quote_author)