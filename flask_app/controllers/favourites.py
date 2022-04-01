from distutils.command import check
from flask import render_template,redirect,session,request, flash
from flask_app import app
import flask_app
from flask_app.models.user import User
from flask_app.models.order import Order
from flask_app.models.cart import Cart
from flask_app.models.favourite import Favourite

# displaying the favourite page
@app.route("/favourite")
def fav_page():
    if 'user_id' not in session:
        return redirect('/signIn')
    data = {
        "id":session['user_id']
    }
    check_favourite = Favourite.get_by_user_id(data)
    print(check_favourite)

    fav = Favourite.get_by_user_id(data)
    print(fav)
    orderlist = Order.get_by_user_id(data)
    return render_template("favourite.html", user=User.get_by_id(data), order=Cart.get_by_user_id(data), items=orderlist, fav=fav)




# adding data to favourite table
@app.route("/add_to_fav/<int:id>")
def add_to_fav(id):
    if 'user_id' not in session:
        return redirect('/signIn')
    
    data = {
        'user_id' : session['user_id'],
        'order_id': id
    }
    print(data)
    Favourite.save(data)
    return redirect('/favourite')


@app.route("/choose_favourite")
def choose_favourite():
    if 'user_id' not in session:
        return redirect('/signIn')
    
    data = {
        'id' : session['user_id']
    }

    fav = Favourite.get_by_user_id(data)
    print(fav)
    orderlist = Order.get_by_user_id(data)
    return render_template("choose_favourite.html", user=User.get_by_id(data), order=Cart.get_by_user_id(data), items=orderlist, fav=fav)