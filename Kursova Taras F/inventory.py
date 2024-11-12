from database import create_connection

def add_product(name, quantity, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))
    conn.commit()
    conn.close()

def update_product(product_id, name, quantity, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET name=?, quantity=?, price=? WHERE id=?', (name, quantity, price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id=?', (product_id,))
    conn.commit()
    conn.close()

def get_product_list():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products
