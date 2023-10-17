#!/usr/bin/env python3
"""
10-update_topics.py

updates the topics of any document specified
"""


def update_topics(mongo_collection, name, topics):
    """
    update_topics(collection, name, topics)

    Args:
      - mongo_collection -> MongoDB collection
      - name -> name of document
      - topics -> list of topics to add

    Returns:
      - None
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
