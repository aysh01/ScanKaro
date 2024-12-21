from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from flask import Blueprint
from pymongo import MongoClient
from datetime import datetime
import random as rd

db_password = "6ruyipcr9R1sCSGh"

monthly_bill = Blueprint('monthly_bill', __name__)

client = MongoClient(
    f"mongodb+srv://aayushkantak01:{db_password}@cluster0.ylmey.mongodb.net/")
db = client['mydb']
collection1 = db['food_items']
collection2 = db['monthly-bills']


def get_monthly_collection():
    current_month = datetime.now().strftime('%Y_%m')
    month = datetime.now().strftime('%m')
    print(current_month, "\n", month)
    return db[f'food_items_{current_month}']


@monthly_bill.route('/')
def index():
    return render_template('monthly_bill.html')


@monthly_bill.route('prevPage1', methods=['POST'])
def index12():
    return render_template('monthly_bill.html')


@monthly_bill.route('food_items')
def next_page():
    return render_template('food_items.html')


@monthly_bill.route('store_items', methods=['POST'])
def add_food_items():
    barcode = request.form.get('barcode')
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')

    total = int(quantity) * float(price)

    food_item = {
        'barcode': barcode,
        'name': name,
        'quantity': quantity,
        'price': price,
        'total': total
    }

    collection1 = get_monthly_collection()
    existing_item = collection1.find_one({'barcode': barcode})

    if existing_item:
        return jsonify({'message': 'Barcode already exists in the database.'}), 200
    else:
        # food_items.append(food_item)
        collection1.insert_one(food_item)  # Insert food items into db..
        print(f"Received Barcode: {food_item}")

        if not barcode:
            return jsonify({'exists': True, 'message': 'Barcode, is required!'}), 400
        else:
            return jsonify({'exists': False, 'message': 'Data saved successfully!'}), 200


@monthly_bill.route('/view_monthly_bill', methods=['GET'])
def view_monthly_bill():
    existing_item = collection2.find_one(
        {'Paid On': {'$exists': True, '$ne': ''}})

    if existing_item:
        invoice_no = existing_item.get('Invoice No')
        return render_template("bills_paid.html", paid=session['paid'][1],
                               month=session.get('month'), date=session.get('date'),
                               invoice=invoice_no)
    else:
        collection1 = get_monthly_collection()
        month = datetime.now().strftime("%B")
        date = datetime.now().strftime("%B %d, %Y")
        time = datetime.now().strftime("%I:%M:%S %p")
        print(date)
        invoice = x = rd.randint(1000, 99999)
        items = list(collection1.find())

        for item in items:
            item['quantity'] = int(item['quantity'])  # Convert to int
            item['price'] = int(item['price'])

            total_cost = sum(int(item['quantity']) *
                             float(item['price']) for item in items)

            paid = ['Paid', 'already Paid']
            session['paid'] = paid

            bills = {
                'Invoice Date': date,
                'Invoice No': invoice,
                'Bill Month': month,
                'Due By': date,
                'Paid On': time,
                'Sub Total': total_cost
            }

            session['bills'] = bills
            session['month'] = month
            session['total_cost'] = total_cost
            session['date'] = date
            session['invoice'] = invoice

            return render_template('view_monthly_bill.html', items=items, total_cost=total_cost,
                                   month=month, time=time, date=date, invoice=invoice)


@monthly_bill.route('pay', methods=['POST'])
def pay():
    bills = session.get('bills')
    total = session.get('total_cost')
    existing_item = collection2.find_one(
        {'Sub Total': total})

    if existing_item:
        invoice_no = existing_item.get('Invoice No')
        return render_template("bills_paid.html", paid=session['paid'][1],
                               month=session.get('month'), date=session.get('date'),
                               invoice=invoice_no)
    else:
        collection2.insert_one(bills)
        return render_template("bills_paid.html", paid=session['paid'][0],
                               month=session.get('month'), date=session.get('date'),
                               invoice=session.get('invoice'))
