#!/usr/bin/env python3
"""
12-log_stats.py

contains the code which reads through a MongoDB collection
and provides us with certains stats.
"""
from pymongo import MongoClient


if __name__ == '__main__':
    methods = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')
    with MongoClient() as client:
        nginx_collection = client.logs.nginx
        print('{} logs'.format(nginx_collection.count_documents({})))
        print('Methods:')
        for method in methods:
            print('\tmethod {}: {}'.format(
                method,
                nginx_collection.count_documents({'method': method})
            ))
        print('{} status check'.format(
            nginx_collection.count_documents({
                'method': 'GET',
                'path': '/status'
            })
        ))
