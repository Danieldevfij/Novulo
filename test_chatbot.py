import re
from novulo_chatbot import find_best_expression


def test_find_valid_until():
    expr, score = find_best_expression("valid_until date of a gift card")
    assert expr is not None
    assert re.search(r"valid_to", expr["expression"]) is not None
