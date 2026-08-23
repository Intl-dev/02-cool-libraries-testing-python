import stripe
from stripe import StripeClient
client = StripeClient("sk_test_BQokikJOvBiI2HlWgH4olfQ2")
customer = client.v1.customers.create({"metadata": {"order_id": "6733"}})
print(customer)
