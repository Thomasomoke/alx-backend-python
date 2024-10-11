#!/usr/bin/env python3
"""
Annotating function"s parameters
return values with appropriate types
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiply(n: float) -> float:
        """Multiplies the input float n by the outer multiplier."""
        return n * multiplier
    return multiply
