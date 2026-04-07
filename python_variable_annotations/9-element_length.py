#!/usr/bin/env python3
"""Annotate function's parameters and return values"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples with elements and their lengths"""
    result = []
    for i in lst:
        result.append((i, len(i)))
    return result
