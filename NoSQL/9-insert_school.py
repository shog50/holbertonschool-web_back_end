#!/usr/bin/env python3
"""Insert a new document into a MongoDB collection using PyMongo"""

from typing import Any


def insert_school(mongo_collection, **kwargs) -> Any:
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: PyMongo collection object.
        **kwargs: Key-value pairs representing document fields.

    Returns:
        The _id of the newly inserted document.
    """
    if mongo_collection is None:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
