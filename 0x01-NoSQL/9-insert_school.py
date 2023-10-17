#!/usr/bin/env python3
"""
9-insert_school.py

Inserts a new document into a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert_school(collection, **kw)

    Args:
      - mongo_collection -> MongoDB collection
      - kwargs -> Python's special keyword args utility

    Returns:
      - the ID of the inserted document
    """
    ack = mongo_collection.insert_one(kwargs)
    return ack.inserted_id
