import sqlite3

def get_total_sales(db_path):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    cursor.execute("SELECT SUM(retail_price) FROM customer_gift_purchases;")
    total = cursor.fetchone()[0] or 0
    con.close()
    return total

db_path = "gift.sqlite"
total_sales = get_total_sales(db_path)
print(f"Išviso pirkimai: {total_sales}")
