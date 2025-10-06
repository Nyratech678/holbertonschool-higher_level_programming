#!/usr/bin/env python3
"""Task 02: Making HTTP Requests with the requests Library"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetches posts and saves id, title, body to posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        # Filter only needed fields
        data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
