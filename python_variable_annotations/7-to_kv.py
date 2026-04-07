#!/usr/bin/env python3
"""Type-annotated function to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> float:
    """Return a tuple with string and square of int/float"""
    return (k, v ** 2)
