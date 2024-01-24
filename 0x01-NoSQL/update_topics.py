#!/usr/bin/env python3
"""A Python function that changes all topics of a
school document based on the name:
Prototype: def update_topics(mongo_collection, name, topics):
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of the school document"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})