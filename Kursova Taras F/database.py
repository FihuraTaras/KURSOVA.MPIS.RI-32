import sqlite3


def create_connection():
    conn = sqlite3.connect('inventory.db')
    return conn


def initialize_db():
    conn = create_connection()
    cursor = conn.cursor()

    # Створення таблиць
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            quantity INTEGER,
            price REAL,
            discount REAL DEFAULT 0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            quantity INTEGER,
            sale_date TEXT,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            role TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            action TEXT,
            timestamp TEXT,
            user_id INTEGER
        )
    ''')

    # Додавання демонстраційних користувачів
    cursor.execute('DELETE FROM users')  # Очистити таблицю перед додаванням
    cursor.executemany('''
        INSERT INTO users (username, password, role) VALUES (?, ?, ?)
    ''', [
        ('admin', 'admin123', 'admin'),
        ('manager', 'manager123', 'manager'),
        ('seller', 'seller123', 'seller')
    ])

    # Додавання демонстраційних товарів
    cursor.execute('DELETE FROM products')  # Очистити таблицю перед додаванням
    cursor.executemany('''
        INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)
    ''', [
        ('Оливки Hacenado ', 50, 300.00),
        ('Тунець в олії Hacenado', 30, 100.00),
        ('Кава в зернах Levazza', 100, 456.00),
        ('Паперові рушники  RUTA', 20, 156.00),
        ('Сік SANDORA (1л)', 15, 100.00)
    ])

    # Додавання демонстраційних продажів
    cursor.execute('DELETE FROM sales')  # Очистити таблицю перед додаванням
    cursor.executemany('''
        INSERT INTO sales (product_id, quantity, sale_date) VALUES (?, ?, ?)
    ''', [
        (1, 5, '2024-11-01'),
        (2, 2, '2024-11-02'),
        (3, 10, '2024-11-03'),
        (4, 1, '2024-11-04'),
        (5, 3, '2024-11-05')
    ])

    conn.commit()
    conn.close()


# Ініціалізація бази даних
initialize_db()
print("База даних успішно ініціалізована з демо-даними.")
