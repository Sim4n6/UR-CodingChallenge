import context
from product1.product import sub


def test_sub():
    assert sub(30, 10) == 20
