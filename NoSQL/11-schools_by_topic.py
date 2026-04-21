#!/usr/bin/env python3
"""
Function that returns the list of school having a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic."""
    query_filter = {'topics': topic}
    result = mongo_collection.find(query_filter)
    return result
