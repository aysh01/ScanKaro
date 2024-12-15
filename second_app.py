from flask import Blueprint
import os
import datetime

autobkup = Blueprint('autobkup', __name__)
db_password = "6ruyipcr9R1sCSGh"

backup_dir = r"C:\\Users\\admin.DESKTOP-4H41SOA\\anaconda3\\Scripts\\venv"
connection_string = f"mongodb+srv://aayushkantak01:{db_password}@cluster0.ylmey.mongodb.net/mydb"


@autobkup.route('/')
def bkup():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    os.makedirs(backup_path, exist_ok=True)

    os.system(f"mongodump --uri \"{connection_string}\" --out \"{backup_path}\"")
    return f"Backup completed at {backup_path}"
