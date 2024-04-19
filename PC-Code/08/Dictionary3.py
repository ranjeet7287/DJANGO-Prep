# Real-time Project Example: Logging System
# Assume a system where logs are stored in a dictionary with timestamps and log messages.
logs = {
    '2022-01-01 12:00': 'System started',
    '2022-01-01 12:15': 'User login',
    '2022-01-01 12:30': 'Data processed successfully'
}
# Iterate through logs using items()
for timestamp, message in logs.items():
    print(f"{timestamp}: {message}")




# Real-time Project Example: User Authentication
# A system where user details are stored in a dictionary, and we want to filter out users above a certain age.
user_details = {
    'Alice': {'age': 25, 'email': 'alice@example.com'},
    'Bob': {'age': 30, 'email': 'bob@example.com'},
    'Charlie': {'age': 22, 'email': 'charlie@example.com'}
}
# Filter users above the age of 25
filtered_users = {name: details for name, details in user_details.items() if details['age'] > 25}
print(filtered_users)



# Real-time Project Example: Product Catalog
# Searching for products based on certain criteria in an e-commerce product catalog.
products = {
    'product1': {'name': 'Laptop', 'price': 1200},
    'product2': {'name': 'Smartphone', 'price': 600},
    'product3': {'name': 'Tablet', 'price': 300}
}
# Search for products with a price below $1000
cheap_products = {key: value for key, value in products.items() if value['price'] < 1000}
print(cheap_products)