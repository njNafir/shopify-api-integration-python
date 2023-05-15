import requests

"""

To get the new Shopify API token, navigate to 

    Settings -> App and sales channel -> Develop apps -> Create an app . 

Choose the Configure Admin API scopes, tick all the checkboxes, and click the Save button. 

Install the App and get the Admin API access token that can be used on the migration wizard.

"""

def fetch_all_orders(api_key, store):
    # Prepare the API endpoint URL
    endpoint = f"https://{store}.myshopify.com/admin/api/2023-04/orders.json"

    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': api_key
    }

    # Send GET request to fetch orders
    response = requests.get(endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the orders from the response
        orders = response.json()['orders']
        return orders
    else:
        # Request was unsuccessful, print error message
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Set your Shopify API credentials and store URL
api_key = "your_api_key"
store_url = "your_store_url"

# Fetch all orders
all_orders = fetch_all_orders(api_key, store_url)

# Print the order details
if all_orders:
    for order in all_orders:
        print(f"Order ID: {order['id']}")
        print(f"Customer Name: {order['customer']['first_name']} {order['customer']['last_name']}")
        print(f"Total Price: {order['total_price']}")
        print("---")
