# Customer Follow-Up Automation
# A simple workflow for identifying customers who need follow-up.

customers = [
    {"name": "Customer A", "status": "needs_follow_up"},
    {"name": "Customer B", "status": "resolved"},
    {"name": "Customer C", "status": "needs_follow_up"},
]

for customer in customers:
    if customer["status"] == "needs_follow_up":
        print(f"Follow up with {customer['name']}")
