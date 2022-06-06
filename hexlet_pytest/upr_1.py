import pytest


@pytest.fixture
def coll():
    return ['One', True, 3, [1, 'hexlet', [0]], 'cat', {}, '', [], False]
