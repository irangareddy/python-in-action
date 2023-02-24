""" Getting Started with Pytest """
import pytest


def test_with_assert():
    """ test one """
    assert [0, 1, 2] != [0, 1, 2]


def test_with_raises():
    """ test one """
    with pytest.raises(AssertionError):
        assert [0, 1, 2] == [1, 0, 2]


def test_passing():
    """ test one """
    assert 2 in [2, 3, 4]
