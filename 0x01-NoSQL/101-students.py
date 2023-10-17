#!/usr/bin/env python3
"""
101-students.py

contains a top_students() method which returns a list
of students sorted by average score
"""


def top_students(mongo_collection):
    """
    top_students(collection)

    Args:
      - mongo_collection -> collection of MongoDB documents

    Returns:
      - list of students sorted by average score
    """
    return mongo_collection.aggregate([
        {
            "$project": {
                "_id": "$_id",
                "name": "$name",
                "averageScore": {
                    # WRONG AND COMPLICATED APPROACH:
                    # "$avg": {
                    #     "$reduce": {
                    #         "input": "$topics",
                    #         "initialValue": {"sum": 0, "count": 0},
                    #         "in": {
                    #             "sum": {
                    #                 "$add": ["$$value.sum", "$$this.score"]
                    #             },
                    #             "count": {
                    #                 "$add": ["$$value.count", 1]
                    #             }
                    #         }
                    #     }
                    # }
                    # CORRECT AND SIMPLE APPROACH:
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])
