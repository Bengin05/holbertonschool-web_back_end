#!/usr/bin/env python3
"""
Function that returns all students sorted by average score.
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Each student document gets an added field "averageScore"
    computed from the values in the "scores" list.

    The results are sorted in descending order of averageScore.
    """
    return mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$scores.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
