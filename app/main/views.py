from flask import render_template,redirect,request,url_for
from . import main
from ..request import get_quotes
from app.models import BlogPost

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    myquote = get_quotes()
    quote = myquote['quote']
    quote_author = myquote['author']
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',quote=quote,quote_author=quote_author, blog_posts=blog_posts)