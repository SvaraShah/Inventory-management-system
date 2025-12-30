import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Helper to connect to the database
def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

# 1. INITIALIZE DATABASE (SAP-Style Schema)
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            threshold INTEGER DEFAULT 5
        )
    ''')
    conn.commit()
    conn.close()

# 2. DISPLAY STOCKS (Read)
@app.route('/')
def index():
    conn = get_db_connection()
    # SQL query to show current stock ledger
    products = conn.execute('SELECT name, sum(quantity) as quantity, price, max(threshold) as threshold FROM products GROUP BY name, price').fetchall()
    conn.close()
    return render_template('index.html', products=products)

# 3. ADD PRODUCT (Stock In)
@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    qty = int(request.form['qty'])
    price = float(request.form['price'])
    
    conn = get_db_connection()
    conn.execute('INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)',
            (name, qty, price))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# 4. REMOVE PRODUCT SIMULATION (Negative Quantity Transaction)
@app.route('/remove', methods=['POST'])
def remove_product():
    name = request.form['name']
    qty = int(request.form['qty'])
    price = float(request.form['price'])
    
    # Simulate Goods Issue by converting quantity to negative
    negative_qty = -abs(qty)
    
    conn = get_db_connection()
    conn.execute('INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)',
                (name, negative_qty, price))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# 5. CLEAN DATABASE (System Reset)
@app.route('/clean', methods=['POST'])
def clean_db():
    conn = get_db_connection()
    conn.execute('DELETE FROM products')
    conn.execute('DELETE FROM sqlite_sequence WHERE name="products"')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)