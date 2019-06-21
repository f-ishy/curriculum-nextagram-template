from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
from models.user import User
from models.donation import Donation
from flask_login import current_user
from instagram_web.util.helpers import client_token, gateway
from braintree import SuccessfulResult 

donate_blueprint = Blueprint('donate',
                            __name__,
                            template_folder='templates')

@donate_blueprint.route('/donate/<receiver_id>', methods=['GET'])
def new(receiver_id):
    return render_template('donate/new.html', client_token=client_token, receiver_id=receiver_id)

@donate_blueprint.route("/checkout", methods=["POST"])
def create():
    nonce_from_the_client = request.form["payment_method_nonce"]
    sender_id = current_user.id
    receiver_id = request.form['receiver_id']
    amount = request.form["amount"]
    result = gateway.transaction.sale({
        "amount": request.form["amount"],
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    if type(result) == SuccessfulResult:
        new_donation = Donation(receiver_id=receiver_id, sender_id = sender_id, amount=amount)
        new_donation.save()
        return redirect(url_for('index'))
    flash('Invalid amount entered!')
    return render_template('donate/new.html', client_token=client_token)
    
