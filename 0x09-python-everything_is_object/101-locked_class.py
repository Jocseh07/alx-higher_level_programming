#!/usr/bin/python3
"""Define a locked class."""


class LockedClass:
    """Prevent user from dynamically creating new instance attributes"""

    __slots__ = ["first_name"]
