#!/usr/bin/env python3
"""
Function that lists all documents in a collection.
"""

def list_all(mongo_collection):
    """ Return an empty list if no document in the collection."""
    if mongo_collection is None:
        return []
    else:
        all_documents = mongo_collection.find({})
    return all_documents
