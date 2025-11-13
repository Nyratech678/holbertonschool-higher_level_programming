#!/usr/bin/python3
"""Flask application to display product data from JSON, CSV, or SQLite."""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(filepath):
    """Read and parse JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        list: List of product dictionaries.
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def read_csv_file(filepath):
    """Read and parse CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        list: List of product dictionaries.
    """
    try:
        products = []
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id to int and price to float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return None
    except (ValueError, KeyError):
        return None


def read_sql_database(db_path):
    """Read and parse data from SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.

    Returns:
        list: List of product dictionaries.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Fetch all products
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()

        # Convert to list of dictionaries
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })

        conn.close()
        return products
    except sqlite3.Error:
        return None
    except Exception:
        return None


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL based on source parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html',
                               error="Wrong source")

    # Read data based on source
    if source == 'json':
        products_data = read_json_file('products.json')
    elif source == 'csv':
        products_data = read_csv_file('products.csv')
    else:  # source == 'sql'
        products_data = read_sql_database('products.db')

    # Check if file/database reading failed
    if products_data is None:
        return render_template('product_display.html',
                               error="Error reading data source")

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data
                                 if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html',
                                       error="Product not found")
            products_data = filtered_products
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid product ID")

    return render_template('product_display.html',
                           products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
