#!/usr/bin/env python3
"""
11-schools_by_topic.py

Returns a list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    schools_by_topic(collection, topic)

    Args:
      - mongo_collection -> a MongoDB collection
      - topic -> topic to use in filtering the results

    Returns:
      - List of schools that match the criteria
    """
    # ONE WAY TO DO IT
    # return mongo_collection.find(
    #     {'topics': {'$elemMatch': {'$eq': topic}}}
    # )

    # ANOTHER WAY TO DO THE SAME THING
    return mongo_collection.find(
        {'topics': {'$eq': topic}}
    )
