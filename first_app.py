from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from flask import Blueprint
from pymongo import MongoClient
from datetime import datetime

db_password = "6ruyipcr9R1sCSGh"

monthly_bill = Blueprint('monthly_bill', __name__)

client = MongoClient(
    f"mongodb+srv://aayushkantak01:{db_password}@cluster0.ylmey.mongodb.net/")
db = client['mydb']
collection1 = db['food_items']


def get_monthly_collection():
    current_month = datetime.now().strftime('%Y_%m')
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
