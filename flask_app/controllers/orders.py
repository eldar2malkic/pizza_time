from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.order import Order
from flask_app.models.cart import Cart

@app.route('/new/order')
def new_company():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id":session['user_id']
    }
    toppings = ["Pepperoni", "Mushroom", "Extra cheese", "Sausage", "Onion", "Black olives", "Green pepper", "Fresh garlic"]
    return render_template('new_ordertest.html',user=User.get_by_id(data), topping=toppings)

@app.route('/create/order',methods=['POST'])
def create_company():
    if 'user_id' not in session:
        return redirect('/')
    non_useful = ['method', 'size', 'crust', 'quantity']
    data = {
        "method": request.form["method"],
        "size": request.form["size"],
        "crust": request.form["crust"],
        "quantity": request.form["quantity"],
        "user_id": session["user_id"]
    }
    topping  = ""
    for key in dict(request.form).keys():
        if key not in non_useful:
            topping = topping + "," + key
    data["topping"] = topping
    order = Order.save(data)
    session['id'] = order
    return redirect('/')


@app.route("/checkout")
def checkout():
    pass