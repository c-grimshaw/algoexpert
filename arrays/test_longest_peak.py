import pytest
from longest_peak import longestPeak


def test_longestPeak():
    assert longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]) == 6
    assert longestPeak([1, 4, 10, 2]) == 4
    assert longestPeak([1, 2, 3]) == 0
    assert longestPeak([1, 2, 2, 0]) == 0
