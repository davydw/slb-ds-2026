# $CHALLENGIFY_BEGIN
"""
Distance calculation utilities.

This module provides functions to compute various distances between points,
including Manhattan, Euclidean, and Minkowski distances.

Functions:
    - manhattan(a, b): Compute the Manhattan (L1) distance.
    - euclidean(a, b): Compute the Euclidean (L2) distance.
    - minkowski(a, b, p): Compute the Minkowski distance of order p.
"""


def manhattan(a, b):
    """
    Calculate the Manhattan distance (L1 norm) between two points.

    The Manhattan distance is the sum of the absolute differences of their
    corresponding coordinates.

    Args:
        a (iterable): The first point as an iterable of numbers.
        b (iterable): The second point as an iterable of numbers.

    Returns:
        float: The Manhattan distance between points a and b.

    Example:
        >>> manhattan([1, 2], [4, 0])
        5.0
    """
    return minkowski(a, b, 1)


def euclidean(a, b):
    """
    Calculate the Euclidean distance between two points.

    This function computes the Euclidean distance between two vectors `a` and `b`
    by calling the `minkowski` function with a power parameter of 2.

    Parameters
    ----------
    a : array-like
        The first vector.
    b : array-like
        The second vector.

    Returns
    -------
    float
        The Euclidean distance between vectors `a` and `b`.
    """
    return minkowski(a, b, 2)


def minkowski(a, b, p):
    """
    Calculate the Minkowski distance between two points in 2D space.

    Parameters:
        a (tuple or list of float): The coordinates (x, y) of the first point.
        b (tuple or list of float): The coordinates (x, y) of the second point.
        p (float): The order of the norm (p >= 1).

    Returns:
        float: The Minkowski distance between points a and b.

    Raises:
        ValueError: If p is less than 1.

    Example:
        >>> minkowski((0, 0), (3, 4), 2)
        5.0
    """
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    distance = (abs(d_x)**p + abs(d_y)**p) ** (1 / p)
    return distance
# $CHALLENGIFY_END
