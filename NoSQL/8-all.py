#!/usr/bin/env python3
"""List all documents in a collection using PyMongo"""

from typing import List


def list_all(mongo_collection) -> List[dict]:
    """
    Returns all documents in a MongoDB collection.

    Args:
        mongo_collection: PyMongo collection object.

    Returns:
        List of documents (empty list if none found).
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
