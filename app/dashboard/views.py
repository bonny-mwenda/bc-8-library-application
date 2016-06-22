from flask import render_template, flash
from flask_login import login_required
from . import dashboard
from .. import db
from ..models import Book
#from .forms import view_books


@dashboard.route('/view_books', methods=['GET', 'POST'])
@login_required
def view_books():
    '''View function to return all books.
    '''
    book = Book.query.all()
    return render_template('dashboard/view_books.html', book=book)