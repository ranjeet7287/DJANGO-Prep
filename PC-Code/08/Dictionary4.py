# 1. Iterating Through Dictionary Keys:
# Real-time Project Example: Database Query
# Assume a scenario where user data is stored in a dictionary, and you need to perform a database query for each user.

# user_data = {
    # 'user1': {'name': 'Alice', 'age': 28, 'city': 'New York'},
    # 'user2': {'name': 'Bob', 'age': 35, 'city': 'San Francisco'},
    # 'user3': {'name': 'Charlie', 'age': 22, 'city': 'Los Angeles'}
# }

# Iterate through user data using keys()
# for user_id in user_data.keys():
#     # Perform a database query for each user using user_id
#     query_result = perform_database_query(user_id)
#     print(f"Query Result for {user_id}: {query_result}")

# # Real-time Project Example: Form Validation
# # Validating form data based on predefined fields.

# form_fields = {'name', 'email', 'phone'}

# Assume a user submits form data
# user_input = {'name': 'Alice', 'email': 'alice@example.com', 'phone': '123-456-7890', 'address': '123 Main St'}

# # Validate form data using keys()
# invalid_fields = [field for field in user_input.keys() if field not in form_fields]
# if invalid_fields:
#     print(f"Invalid fields: {', '.join(invalid_fields)}")
# else:
#     print("Form data is valid.")
