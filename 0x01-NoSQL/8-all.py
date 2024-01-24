#!/usr/bin/env python3
"""
A script that return a list of all collections
"""

import pymongo



def list_all(mongo_collection):
    """Return list of all the docs in the collection"""
    if not mongo_collection:
        return []
    doc = mongo_collection.find()
    return [document for document in doc]