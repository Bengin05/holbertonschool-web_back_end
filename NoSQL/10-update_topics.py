#!/usr/bin/env python3
"""
Function that changes all topics of a school document based on the name.
"""

def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name."""
    query_filter = {'name': name}
    update_topics = {'$set': {'topics': topics}}

    result = mongo_collection.update_many(query_filter, update_topics)
