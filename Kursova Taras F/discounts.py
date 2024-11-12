from database import create_connection

def set_discount(product_id, discount):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET discount=? WHERE id=?', (discount, product_id))
    conn.commit()
    conn.close()

def get_discounted_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE discount > 0')
    products = cursor.fetchall()
    conn.close()
    return products
