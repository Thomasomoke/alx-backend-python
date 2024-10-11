#!/usr/bin/env python3
"""
A type-annotated function to_kv that takes a string k
and an int or float v as arguments and returns a tuple.
The first element is the string k, and the second element is
the square of the int/float v (annotated as a float).
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is the string k
    and the second element is the square of v, annotated as a float."""
    return (k, float(v ** 2))
