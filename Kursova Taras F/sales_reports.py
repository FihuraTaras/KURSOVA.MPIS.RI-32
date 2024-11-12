from database import create_connection

def generate_sales_report():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT products.name, SUM(sales.quantity) AS total_sold, SUM(sales.quantity * products.price) AS total_income
        FROM sales
        JOIN products ON products.id = sales.product_id
        GROUP BY products.id
    ''')
    report = cursor.fetchall()
    conn.close()
    return report
