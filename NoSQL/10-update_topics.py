#!/usr/bin/env python3
"""Update the topics field of a school document based on its name using PyMongo"""


def update_topics(mongo_collection, name: str, topics: list):
    """
    Updates the topics of a school document identified by name.

    Args:
        mongo_collection: PyMongo collection object.
        name (str): Name of the school to update.
        topics (list of str): List of topics to set in the document.
    """
    if mongo_collection is None:
        return

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
