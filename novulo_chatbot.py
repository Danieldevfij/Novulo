"""Simple chatbot to suggest Novulo expressions based on user goals."""

from difflib import SequenceMatcher

# Database of known Novulo expressions. Each item has a description
# that explains the goal and the expression itself.
EXPRESSIONS = [
    {
        "description": "find the valid_until date of a gift card",
        "expression": "date:max({giftcardshoppingcarts,this.gift_card.valid_to,this.shopping_cart.equals(parent)})",
    },
    {
        "description": "sum the amounts of all order lines",
        "expression": "sum({orderlines,this.amount})",
    },
]


def find_best_expression(query: str):
    """Return the expression whose description best matches the query."""
    query = query.lower()
    best = None
    best_score = 0.0
    for item in EXPRESSIONS:
        score = SequenceMatcher(None, query, item["description"].lower()).ratio()
        if score > best_score:
            best_score = score
            best = item
    return best, best_score


def chat():
    print("Novulo Expression Assistant")
    print("Type 'exit' to quit")
    while True:
        try:
            user_input = input("User: ")
        except EOFError:
            break
        if not user_input:
            continue
        if user_input.strip().lower() in {"exit", "quit"}:
            print("Goodbye")
            break
        expr, score = find_best_expression(user_input)
        if expr:
            print("Bot Suggestion:")
            print(expr["expression"])
        else:
            print("Sorry, I don't know a matching expression yet.")


if __name__ == "__main__":
    chat()
