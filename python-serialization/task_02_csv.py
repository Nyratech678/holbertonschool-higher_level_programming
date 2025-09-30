#!/usr/bin/python3
"""Convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON file named 'data.json'.

    Args:
        csv_filename (str): input CSV filename

    Returns:
        bool: True if successful, False if error occurs
    """
    try:
        data = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
