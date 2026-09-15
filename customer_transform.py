"""Simple data-engineering practice script."""

customers = [
    {"customer_id": 101, "name": "JOHN", "state": "NC"},
    {"customer_id": 102, "name": "sarah", "state": "NY"},
    {"customer_id": 101, "name": "JOHN", "state": "NC"},
]

unique = {}
for customer in customers:
    cleaned = customer.copy()
    cleaned["name"] = cleaned["name"].title()
    unique[cleaned["customer_id"]] = cleaned

print(list(unique.values()))
