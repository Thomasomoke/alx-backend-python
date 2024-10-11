#!/usr/bin/env python3
"""
a type-annotated function make_multiplier
returns a function that multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(n: float) -> float:
        """Multiplies the input float n by the outer multiplier"""
        return n * multiplier
    return multiply
