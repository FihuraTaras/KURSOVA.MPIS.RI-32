import tkinter as tk
from tkinter import messagebox
from inventory import get_product_list, add_product, update_product, delete_product
from sales_reports import generate_sales_report
from discounts import get_discounted_products, set_discount
from access_control import add_user, authenticate_user
from logs import add_log
from database import create_connection


def generate_inventory_report():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    report = cursor.fetchall()
    conn.close()
    return report


def view_inventory_report():
    report = generate_inventory_report()
    report_window = tk.Toplevel()
    report_window.title("Інвентаризаційний звіт")
    text = tk.Text(report_window, width=60, height=20)
    text.pack()
    for item in report:
        text.insert(tk.END, f"ID: {item[0]}, Назва: {item[1]}, Кількість: {item[2]}, Ціна: {item[3]} грн\n")


def view_sales_report():
    report = generate_sales_report()
    report_window = tk.Toplevel()
    report_window.title("Звіт по продажах")
    text = tk.Text(report_window, width=60, height=20)
    text.pack()
    for item in report:
        text.insert(tk.END, f"Товар: {item[0]}, Продано: {item[1]} шт, Доход: {item[2]} грн\n")


def manage_discounts():
    discount_window = tk.Toplevel()
    discount_window.title("Керування знижками")

    def apply_discount():
        try:
            product_id = int(entry_product_id.get())
            discount = float(entry_discount.get())
            set_discount(product_id, discount)
            messagebox.showinfo("Успіх", "Знижку успішно встановлено!")
        except ValueError:
            messagebox.showerror("Помилка", "Невірний формат введених даних")

    tk.Label(discount_window, text="ID Товару").pack()
    entry_product_id = tk.Entry(discount_window)
    entry_product_id.pack()

    tk.Label(discount_window, text="Знижка (%)").pack()
    entry_discount = tk.Entry(discount_window)
    entry_discount.pack()

    tk.Button(discount_window, text="Встановити знижку", command=apply_discount).pack()


def manage_inventory():
    inventory_window = tk.Toplevel()
    inventory_window.title("Управління запасами")

    def refresh_product_list():
        products = get_product_list()
        listbox.delete(0, tk.END)
        for product in products:
            listbox.insert(tk.END, f"{product[1]} - {product[2]} шт - {product[3]} грн")

    listbox = tk.Listbox(inventory_window, width=50)
    listbox.pack()

    btn_refresh = tk.Button(inventory_window, text='Оновити список', command=refresh_product_list)
    btn_refresh.pack()

    refresh_product_list()


def user_access_control():
    access_window = tk.Toplevel()
    access_window.title("Управління доступом")

    def add_new_user():
        username = entry_username.get()
        password = entry_password.get()
        role = entry_role.get()
        add_user(username, password, role)
        messagebox.showinfo("Успіх", "Користувача додано!")

    tk.Label(access_window, text="Ім'я користувача").pack()
    entry_username = tk.Entry(access_window)
    entry_username.pack()

    tk.Label(access_window, text="Пароль").pack()
    entry_password = tk.Entry(access_window, show="*")
    entry_password.pack()

    tk.Label(access_window, text="Роль").pack()
    entry_role = tk.Entry(access_window)
    entry_role.pack()

    tk.Button(access_window, text="Додати користувача", command=add_new_user).pack()


def view_logs():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logs')
    logs = cursor.fetchall()
    conn.close()

    logs_window = tk.Toplevel()
    logs_window.title("Історія змін")
    text = tk.Text(logs_window, width=60, height=20)
    text.pack()
    for log in logs:
        text.insert(tk.END, f"ID: {log[0]}, Дія: {log[1]}, Час: {log[2]}, ID користувача: {log[3]}\n")


def start_app():
    root = tk.Tk()
    root.title('Система управління інвентарем')

    # Меню
    menu_bar = tk.Menu(root)

    # Меню управління
    manage_menu = tk.Menu(menu_bar, tearoff=0)
    manage_menu.add_command(label="Управління запасами товарів", command=manage_inventory)
    manage_menu.add_command(label="Моніторинг залишків товарів", command=view_inventory_report)
    menu_bar.add_cascade(label="Управління", menu=manage_menu)

    # Меню звітів
    reports_menu = tk.Menu(menu_bar, tearoff=0)
    reports_menu.add_command(label="Звіт по продажах", command=view_sales_report)
    reports_menu.add_command(label="Інвентаризаційний звіт", command=view_inventory_report)
    menu_bar.add_cascade(label="Звіти", menu=reports_menu)

    # Меню знижок та акцій
    discounts_menu = tk.Menu(menu_bar, tearoff=0)
    discounts_menu.add_command(label="Керування знижками та акціями", command=manage_discounts)
    menu_bar.add_cascade(label="Знижки та акції", menu=discounts_menu)

    # Меню доступу
    access_menu = tk.Menu(menu_bar, tearoff=0)
    access_menu.add_command(label="Управління доступом користувачів", command=user_access_control)
    access_menu.add_command(label="Історія змін", command=view_logs)
    menu_bar.add_cascade(label="Доступ", menu=access_menu)

    # Встановити меню в головне вікно
    root.config(menu=menu_bar)

    root.mainloop()


if __name__ == '__main__':
    start_app()
