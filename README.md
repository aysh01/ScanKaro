# Developing a Skc+ (ScanKaro+) | Food Barcode Scanner App

## Installation

Use the package manager [pip](https://docs.python.org/3/installing/index.html) to install all the necessary dependencies.

## To work with the packages, you have to install them. You can do this by using the command prompt or terminal.

Type this command 👇
```python
pip install -r requirements.txt
```

## Necessary Packages for this project ..
```Flask```
```render_template```
```request``` ```jsonify``` ```redirect``` ```url_for``` ```session```
```MongoClient``` ```Blueprint``` ```datetime```

## Do Make Sure that you've created a [MongoDB Atlas Cluster](https://www.mongodb.com/atlas) and have connected it to [MongoDB Compass](https://www.mongodb.com/try/download/community) ( Use, compass if required for better UI ) ..

## Also, don't forget to import json files into your Db ..
## Usage

Inside venv directory
```python
C:\Users\Scripts\venv>cd Scripts
```
Then, type command ```activate``` .
```python
C:\Users\Scripts\venv\Scripts>activate
```
It, will start Python Virtual-Environment [venv](https://python.land/virtual-environments/virtualenv).
```Python
(venv) C:\Users\Scripts\venv\Scripts>
```
Then, go to previous directory ```venv```
```Python
(venv) C:\Users\Scripts\venv\Scripts>cd..

(venv) C:\Users\Scripts\venv>
```
Run the Program 👇
```Python
(venv) C:\Users\Scripts\venv>py form.py
 * Serving Flask app 'form'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```
To, close the ```venv```.
```python
(venv) C:\Users\Scripts\venv>cd Scripts

(venv) C:\Users\Scripts\venv\Scripts>
```
Then, type command ```deactivate``` .
```python
(venv) C:\Users\Scripts\venv\Scripts>deactivate

C:\Users\Scripts\venv\Scripts>
```
It, will stop Python Virtual-Environment.

## Video Explanation
<a href="">
<img src="https://github.com/aysh01/ScanKaro/blob/main/static/Scan-barcode.png" alt="Image">
</a>

## Output
![Scan-barcode](https://github.com/aysh01/ScanKaro/blob/main/static/Scan-barcode.png)
![Scan-barcode-details](https://github.com/aysh01/ScanKaro/blob/main/static/Scan-barcode-details.png)
![Scan-barcode-details-in-db](https://github.com/aysh01/ScanKaro/blob/main/static/Scan-barcode-details-in-db.png)
![monthly-bill](https://github.com/aysh01/ScanKaro/blob/main/static/monthly-bill.png)
![monthly-bill-details](https://github.com/aysh01/ScanKaro/blob/main/static/monthly-bill-details.png)
![monthly-bill-details-in-db](https://github.com/aysh01/ScanKaro/blob/main/static/monthly-bill-details-in-db.png)


## License

[MIT License](https://github.com/aysh01/Web_Scrapper/blob/main/LICENSE)



