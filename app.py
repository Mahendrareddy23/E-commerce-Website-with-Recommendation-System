from flask import Flask, jsonify
import sqlite3
from recommendation import get_recommendations

app = Flask(__name__)

def get_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM producdcts")
    products = cursor.fetchall()
    conn.close()
    return products

@app.route('/api/products', methods=['GET'])
def api_products():
    products = get_products()
    return jsonify(products)

@app.route('/api/recommendations/<int:user_id>', methods=['GET'])
def api_recommendations(user_id):
    recommendations = get_recommendations(user_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
