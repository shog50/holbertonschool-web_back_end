#!/usr/bin/env python3
"""Return the list of schools having a specific topic using PyMongo"""


from typing import List, Any


def schools_by_topic(mongo_collection, topic: str) -> List[Any]:
    """
    Returns all schools that have the specified topic.

    Args:
        mongo_collection: PyMongo collection object.
        topic (str): Topic to search for.

    Returns:
        List of documents (schools) that contain the topic.
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find({"topics": topic}))
