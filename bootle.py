""" “Should array indices start at 0 or 1? My compromise of 0.5 was rejected
without, I thought, proper consideration.” — Stan Kelly-Bootle
"""

import math

__all__ = ["List"]
__version__ = "0.1.1"


def _transform_index(index, allow_none=False):
    if index is None and allow_none:
        return None
    if isinstance(index, slice):
        try:
            return slice(
                _transform_index(index.start, allow_none=True),
                _transform_index(index.stop, allow_none=True),
                index.step,
            )
        except TypeError:
            raise TypeError("slice indices must be floats or None")
    if not isinstance(index, float):
        raise TypeError(
            "half-indexed indices must be floats or slices, not {}".format(
                type(index).__name__
            )
        )
    if index % 1 != 0.5:
        raise ValueError("half-indexed indices must have a 0.5 fractional component")
    return math.floor(index)


class List(list):
    """A subclass of list that is indexed from 0.5."""

    def __delitem__(self, key):
        """Delete self[key]."""
        return super().__delitem__(_transform_index(key))

    def __getitem__(self, key):
        """Return self[key]."""
        value = super().__getitem__(_transform_index(key))
        return self.__class__(value) if isinstance(key, slice) else value

    def __setitem__(self, key, value):
        """Set self[key] to value."""
        return super().__setitem__(_transform_index(key), value)

    def index(self, value, start=0.5, stop=4503599627370495.5):
        """Return first index of value."""
        n = super().index(value, _transform_index(start), _transform_index(stop))
        return n + 0.5

    def insert(self, index, value):
        """Insert object before index."""
        return super().insert(_transform_index(index), value)

    def pop(self, index=-0.5):
        """Remove and return item at index (default last)."""
        return super().pop(_transform_index(index))
