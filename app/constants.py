"""
constants.py
-------------

Contains constants used throughout the project.
"""

# List of valid country codes
VALID_COUNTRY_LIST = ["91", "45", "67", "56"]

# List of excluded mobile numbers
EXCLUDED_NUMBERS = ["9898989898", "9999999999", "8888888888"]

# List of valid genders
VALID_GENDERS = ["male", "female", "other"]

# List of valid blood groups
VALID_BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

# Log switch (True to enable logging, False to disable)
LOG_SWITCH = True

# Validation patterns
EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
MOBILE_PATTERN = r'^\d{10}$'

# Log messages
LOG_MESSAGES = {
    'error': "Error: {message}",
    'info': "Info: {message}",
    'warning': "Warning: {message}",
    'critical': "Critical: {message}",
}

# Example log messages
VALID_EMAIL_LOG = "Valid email: {email}"
INVALID_EMAIL_LOG = "Invalid email format: {email}"
VALID_AGE_LOG = "Valid age: {age}"
INVALID_AGE_LOG = "Invalid age: {age}"
VALID_MOBILE_LOG = "Valid mobile number: {mobile}"
INVALID_MOBILE_LOG = "Invalid mobile number: {mobile}"
EXCLUDED_MOBILE_LOG = "Excluded mobile number: {mobile}"
VALID_GENDER_LOG = "Valid gender: {gender}"
INVALID_GENDER_LOG = "Invalid gender: {gender}"
VALID_BLOOD_GROUP_LOG = "Valid blood group: {blood_group}"
INVALID_BLOOD_GROUP_LOG = "Invalid blood group: {blood_group}"
USER_INFO_LOG = "User info for {username}: {user_info}"
UNAUTHORIZED_ACCESS_LOG = "Unauthorized access attempt by {current_user} to view {username}'s information"
USER_NOT_FOUND_LOG = "User {username} not found"
ADMIN_LIST_USERS_LOG = "Admin {current_user} listing all users"
LIST_USERS_ERROR_LOG = "Unauthorized access attempt by {current_user} to list all users"
