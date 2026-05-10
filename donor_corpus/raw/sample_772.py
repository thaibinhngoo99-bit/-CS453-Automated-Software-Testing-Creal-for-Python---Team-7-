import unittest
from repeater import repeater


def test_repeater(benchmark):
    assert benchmark(repeater,'a',5) == 'aaaaa'
    assert benchmark(repeater,'Wub', 6 ) == 'Wub Wub Wub Wub Wub Wub '
