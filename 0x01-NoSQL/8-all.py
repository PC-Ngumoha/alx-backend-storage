#!/usr/bin/env python3
"""
8-all.py

Lists all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """
    list_all(collection)

    Args:
      - mongo_collection -> a collection in MongoDB

    Returns:
      - list of all document objects in the collection
    """
    return mongo_collection.find({})
