#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def print_nginx_stats():
    """
    Print statistics about Nginx logs stored in MongoDB.

    This function connects to the MongoDB server running on localhost,
    retrieves log entries from the 'nginx' collection, and displays:
        - Total number of log documents
        - Count of each HTTP method (GET, POST, PUT, PATCH, DELETE)
        - Count of GET requests to the /status path
    """
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection = db.nginx

    total = collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

if __name__ == "__main__":
    print_nginx_stats()
