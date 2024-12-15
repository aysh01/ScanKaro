from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from pymongo import MongoClient
from first_app import monthly_bill
from second_app import autobkup
import bcrypt

db_password = "6ruyipcr9R1sCSGh"

app = Flask(__name__)

app.register_blueprint(monthly_bill, url_prefix='/monthly_bill')
app.register_blueprint(autobkup, url_prefix='/autobkup')

client = MongoClient(
    f"mongodb+srv://aayushkantak01:{db_password}@cluster0.ylmey.mongodb.net/")
db = client['mydb']
collection = db['users']

app.secret_key = "testing"


@app.route("/", methods=['post', 'get'])
def index():
    message = ''
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # if found in database showcase that it's found
        user_found = collection.find_one({"name": user})
        email_found = collection.find_one({"email": email})

        if user_found:
            message = 'There already is a user by that name'
            return render_template('form.html', message=message)

        if email_found:
            message = 'This email already exists in database'
            return render_template('form.html', message=message)

        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('form.html', message=message)

        else:
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            user_input = {'name': user, 'email': email, 'password': hashed}
            collection.insert_one(user_input)
            message = 'Thank You! Your, account is created successfully .)'

            # find the new created account and its email
            user_data = collection.find_one({"email": email})
            new_email = user_data['email']

            return render_template('login.html', email=new_email)

    return render_template('form.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # check if email exists in database
        email_found = collection.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']

            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('logged_in'))

            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message = 'Wrong password'

                return render_template('login.html', message=message)

        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)


@app.route('/logged_in')
def logged_in():
    if "email" in session:
        email = session["email"]
        message = f'Hello You have Logged in as {email}'

        return render_template('main.html', email=email)
    else:
        return redirect(url_for("login"))


@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("signout.html")
    else:
        return render_template('base.html')


@app.route('/check_session', methods=['GET'])
def check_session():
    if 'email' in session:
        return jsonify(active=True)
    return jsonify(active=False)


@app.route('/food_details', methods=['POST'])
def index1():
    return render_template('logged_in.html')


@app.route('/prevPage', methods=['POST'])
def index12():
    return render_template('main.html')


@app.route('/add_food', methods=['POST'])
def add_food():
    barcode = request.form.get('barcode')
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')

    food_item = {
        'barcode': barcode,
        'name': name,
        'quantity': quantity,
        'price': price
    }

    existing_item = collection.find_one({'barcode': barcode})

    if existing_item:
        return jsonify({'message': 'Barcode already exists in the database.'}), 200
    else:
        # food_items.append(food_item)
        collection.insert_one(food_item)  # Insert food items into db..
        print(f"Received Barcode: {food_item}")

        if not barcode:
            return jsonify({'exists': True, 'message': 'Barcode, is required!'}), 400
        else:
            return jsonify({'exists': False, 'message': 'Data saved successfully!'}), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
