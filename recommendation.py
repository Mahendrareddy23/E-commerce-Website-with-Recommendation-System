# backend/recommendation.py
import sqlite3

def get_recommendations(user_id):
    # Dummy recommendation logic (e.g., recommend the first 3 products)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products LIMIT 3")
    recommendations = cursor.fetchall()
    conn.close()
    return recommendations
