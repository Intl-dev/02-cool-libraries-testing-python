import stripe
from stripe import StripeClient
import os
import dotenv
dotenv.load_dotenv()
stripe_client = os.getenv('STRIPE_CLIENT')
client = StripeClient(stripe_client)
customer = client.v1.customers.create({"metadata": {"order_id": "6733"}})
print(customer)
