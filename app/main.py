"""
main.py
--------
Demonstrates various user scenarios including admin and normal user actions.
"""

from utils import get_user_info, list_all_users, validate_args
from log import *
from data import *

def main():
    """
    Main function demonstrating various user scenarios.
    """
    # Scenario 1: Admin viewing a specific user information
    try:
        admin_username = "kiran"
        user_to_view = "radha"  # Corrected the username to match an existing user
        user_info = get_user_info(user_to_view, admin_username, is_admin=True)
        print(f"Admin {admin_username} viewed user {user_to_view}: {user_info}")
    except (ValueError, PermissionError) as e:
        log_message('critical', str(e))

    # Scenario 2: Admin listing all users
    try:
        admin_username = "kiran"  # Corrected to a valid admin user
        all_users = list_all_users(admin_username, is_admin=True)
        print(f"Admin {admin_username} listed all users: {all_users}")
    except (ValueError, PermissionError) as e:
        log_message('critical', str(e))

    # Scenario 3: Normal user trying to view their own information
    try:
        normal_username = "radha"  # Corrected to a valid normal user
        user_info = get_user_info(normal_username, normal_username, is_admin=False)
        print(f"Normal user {normal_username} viewed their information: {user_info}")
    except (ValueError, PermissionError) as e:
        log_message('critical', str(e))

    # Scenario 4: Normal user trying to view another user's information
    try:
        normal_username = "radha"
        user_to_view = "kiran"  # Trying to access another user's info
        get_user_info(user_to_view, normal_username, is_admin=False)
    except (ValueError, PermissionError) as e:
        log_message('critical', str(e))  # Expecting a PermissionError

    # Scenario 5: Admin trying to view a non-existent user's information
    try:
        admin_username = "kiran"
        user_to_view = "non_existent_user"
        get_user_info(user_to_view, admin_username, is_admin=True)
    except (ValueError, PermissionError) as e:
        log_message('critical', str(e))  # Expecting a ValueError

    # Scenario 6: Admin adding a new user
    try:
        new_user_info = {
            "email": "newuser@example.com",
            "age": 28,
            "mobile": "1234567890",
            "gender": "other",
            "blood_group": "AB+",
            "role": "user"
        }
        user_data.add_user("new_user", new_user_info)
        log_message('info', "Admin added a new user: new_user")
    except Exception as e:
        log_message('error', f"Error adding new user: {e}")

    # Scenario 7: Validating various inputs
    try:
        validate_args(email="test@example.com", age=30, mobile="1234567890", gender="female", blood_group="O+")
        print("All validations passed successfully")
    except (ValueError, TypeError) as e:
        log_message('error', f"Validation error: {e}")

# Run the main function
if __name__ == "__main__":
    main()
