#!/usr/bin/env python3
"""
102-log_stats.py

contains the code which reads through a MongoDB collection
and provides us with certains stats. This is an improvement on
what we did in the 12-log_stats.py file. The major improvement
in this version stemming from the fact that we also try to list out
the top 10 most present IP addresses in addition to other stats.
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
        top_ips = nginx_collection.aggregate([
            {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
            {'$sort': {'count': -1}},
            {'$limit': 10}
        ])
        print('IPs:')
        for ip in top_ips:
            print('\t{}: {}'.format(ip.get('_id'), ip.get('count')))
