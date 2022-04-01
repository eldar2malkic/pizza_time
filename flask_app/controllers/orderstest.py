from flask import render_template,redirect,session,request, flash
import random
from flask_app import app
from flask_app.models.user import User
from flask_app.models.order import Order
from flask_app.models.cart import Cart
from flask_app.models.special import Special

@app.route('/specials')
def specials():
    if 'user_id' not in session:
        return redirect('/')
    specials = Special.get_all()
    random_special = random.randint(0,len(specials)-1)

    chosen = specials[random_special]
    data = {
        "method": chosen["method"],
        "size": chosen["size"],
        "topping": chosen["topping"],
        "crust": chosen["crust"],
        "quantity": chosen["quantity"],
        "user_id": session["user_id"]
    }
    Cart.save(data)
    return redirect('/checkout')

@app.route('/new/order')
def order():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id":session['user_id']
    }
    return render_template('new_ordertest.html', user=User.get_by_id(data), order=Cart.get_by_user_id(data))

@app.route('/create/order',methods=['POST'])
def new_order():
    if 'user_id' not in session:
        return redirect('/register')
    
    toppingList = request.form.getlist("topping")
    toppings = " ".join(map(str,toppingList))
    print(toppings)
    data = {
        "method": request.form["method"],
        "size": request.form["size"],
        "crust": request.form["crust"],
        "quantity": request.form["quantity"],
        "topping": toppings,
        "user_id": session["user_id"]
    }
    print(data)
    Cart.save(data)
    return redirect('/')
    
@app.route('/checkout')
def checkout():
    if 'user_id' not in session:
        return redirect('/register')

    data = {
        "id":session['user_id']
    }
    orderlist = Cart.get_by_user_id(data)
    pricelist = []
    price = 0
    for order in orderlist:
        if order['size'] == 'MEDIUM':
            price = price+7
        elif order['size'] == 'LARGE':
            price = price+10
        elif order['size'] == 'SMALL':
            price = price+5
        elif order['size'] == 'Extra-large':
            price = price+15

        price = price*int(order['quantity'])
        pricelist.append(price)
        price = 0

    print(orderlist)
    print(pricelist)
    return render_template('checkout.html', user=User.get_by_id(data), items=orderlist, price=pricelist, order=Cart.get_by_user_id(data))

@app.route("/checkout/order")
def checkout_order():
    if 'user_id' not in session:
        return redirect('/signIn')

    data = {
        "id":session['user_id']
    }
    orders = Cart.get_by_user_id(data)
    if orders:
        for order in orders:
            order_data = {}

            order_data = {
            "method": order['method'],
            "size": order["size"],
            "crust": order["crust"],
            "quantity": order["quantity"],
            "topping": order['topping'],
            "user_id": order["user_id"]
            }
            Order.save(order_data)

            id = {
                "id": order['id']
            }
            Cart.delete(id)   
    return redirect("/")

@app.route("/delete/cart_item/<int:id>")
def delete_cart_item(id):
    if 'user_id' not in session:
        return redirect('/signIn')
    data = {
        "id": id
    }
    Cart.delete(data)
    return redirect('/checkout')

@app.route("/order_again/<int:id>")
def order_again(id):
    if 'user_id' not in session:
        return redirect('/signIn')
    
    data = {
        "id": id
    }
    
    order = Order.get_by_id(data)
    print(order)
    order_data = {
            "method": order['method'],
            "size": order["size"],
            "crust": order["crust"],
            "quantity": order["quantity"],
            "topping": order['topping'],
            "user_id": order["user_id"]
            }
    Cart.save(order_data)
    return redirect('/checkout')

@app.route('/edit/<int:order_id>')
def edit(order_id):
    data = {
        'id': order_id,
    }
    data1 = {
        'id': session['user_id']
    }
    return render_template("edit_order.html", user=User.get_by_id(data1), edit_cart = Cart.get_by_id(data), order=Cart.get_by_user_id(data1))


@app.route('/update/<int:order_id>', methods =['POST'])
def update(order_id):
    if 'user_id' not in session:
        return redirect('/register')
    
    toppingList = request.form.getlist("topping")
    toppings = " ".join(map(str,toppingList))
    print(toppings)
    data = {
        "id": order_id,
        "method": request.form["method"],
        "size": request.form["size"],
        "crust": request.form["crust"],
        "quantity": request.form["quantity"],
        "topping": toppings,
        "user_id": session["user_id"]
    }
    print(data)

    Cart.update(data)

    return redirect('/checkout')