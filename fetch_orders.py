import requests

"""

1. API Key: 
    This is a unique identifier for your Shopify app. 
    It is generated when you create the app in the Shopify Partner Dashboard. 
    The API key is used to identify your app when making API requests.

2. Password: 
    The password is an API-specific password that is associated with the Shopify store. 
    It is different from your Shopify account password. 
    You can generate an API password by following these steps:

    * Log in to your Shopify admin.
    * Go to "Apps" in the sidebar.
    * Scroll down to the "Manage private apps" section.
    * Click on "Create a new private app" or select an existing private app.
    * In the "Admin API" section, you'll find the "Password" field. 
        This is the password you'll use for authentication in API requests.

"""

def fetch_all_orders(api_key, password, store_url):
    # Prepare the API endpoint URL
    endpoint = f"https://{api_key}:{password}@{store_url}/admin/api/2023-04/orders.json"

    # Send GET request to fetch orders
    response = requests.get(endpoint)

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
password = "your_password"
store_url = "your_store_url.myshopify.com"

# Fetch all orders
all_orders = fetch_all_orders(api_key, password, store_url)

# Print the order details
if all_orders:
    for order in all_orders:
        print(f"Order ID: {order['id']}")
        print(f"Customer Name: {order['customer']['first_name']} {order['customer']['last_name']}")
        print(f"Total Price: {order['total_price']}")
        print("---")
