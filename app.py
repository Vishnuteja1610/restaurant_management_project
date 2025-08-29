from flask import Flask, session, render_template
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def home():
    cart = session.get('cart',{})
    total_items = sum(cart.values())
    return render_template('home.html',total_items=total_items)
    