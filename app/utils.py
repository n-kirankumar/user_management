"""
utils.py
---------
Contains utility functions for validating user data and retrieving user information.
"""

import re
from log import log_message
from constants import (
    EMAIL_PATTERN,
    MOBILE_PATTERN,
    VALID_COUNTRY_LIST,
    EXCLUDED_NUMBERS,
    VALID_GENDERS,
    VALID_BLOOD_GROUPS,
    VALID_EMAIL_LOG,
    INVALID_EMAIL_LOG,
    VALID_AGE_LOG,
    INVALID_AGE_LOG,
    VALID_MOBILE_LOG,
    INVALID_MOBILE_LOG,
    EXCLUDED_MOBILE_LOG,
    VALID_GENDER_LOG,
    INVALID_GENDER_LOG,
    VALID_BLOOD_GROUP_LOG,
    INVALID_BLOOD_GROUP_LOG,
    USER_INFO_LOG,
    UNAUTHORIZED_ACCESS_LOG,
    USER_NOT_FOUND_LOG,
    ADMIN_LIST_USERS_LOG,
    LIST_USERS_ERROR_LOG
)

def validate_email(email):
    """
    Validates the given email address.
    """
    if not re.match(EMAIL_PATTERN, email):
        log_message('error', INVALID_EMAIL_LOG, email=email)
        raise ValueError("Invalid email format")
    log_message('info', VALID_EMAIL_LOG, email=email)
    return True

def validate_age(age):
    """
    Validates the given age.
    """
    if not (0 <= age <= 120):
        log_message('error', INVALID_AGE_LOG, age=age)
        raise ValueError("Invalid age")
    log_message('info', VALID_AGE_LOG, age=age)
    return True

def validate_mobile(mobile):
    """
    Validates the given mobile number.
    """
    if not re.match(MOBILE_PATTERN, mobile):
        log_message('error', INVALID_MOBILE_LOG, mobile=mobile)
        raise ValueError("Invalid mobile number")
    if mobile in EXCLUDED_NUMBERS:
        log_message('info', EXCLUDED_MOBILE_LOG, mobile=mobile)
        return False
    log_message('info', VALID_MOBILE_LOG, mobile=mobile)
    return True

def validate_gender(gender):
    """
    Validates the given gender.
    """
    if gender.lower() not in VALID_GENDERS:
        log_message('error', INVALID_GENDER_LOG, gender=gender)
        raise ValueError("Invalid gender")
    log_message('info', VALID_GENDER_LOG, gender=gender)
    return True

def validate_blood_group(blood_group):
    """
    Validates the given blood group.
    """
    if blood_group.upper() not in VALID_BLOOD_GROUPS:
        log_message('error', INVALID_BLOOD_GROUP_LOG, blood_group=blood_group)
        raise ValueError("Invalid blood group")
    log_message('info', VALID_BLOOD_GROUP_LOG, blood_group=blood_group)
    return True

def get_user_info(username, current_user, is_admin):
    """
    Retrieves information for the specified user.
    """
    from data import user_data
    user_info = user_data.get_user(username)
    if user_info:
        if username == current_user or is_admin:
            log_message('info', USER_INFO_LOG, username=username, user_info=user_info)
            return user_info
        else:
            log_message('warning', UNAUTHORIZED_ACCESS_LOG, current_user=current_user, username=username)
            raise PermissionError("Unauthorized access")
    else:
        log_message('error', USER_NOT_FOUND_LOG, username=username)
        raise ValueError("User not found")

def list_all_users(current_user, is_admin):
    """
    Lists all users if the requester is an admin.
    """
    from data import user_data
    if is_admin:
        log_message('info', ADMIN_LIST_USERS_LOG, current_user=current_user)
        return user_data.records
    else:
        log_message('warning', LIST_USERS_ERROR_LOG, current_user=current_user)
        raise PermissionError("Unauthorized access")

# Decorators for validation

def validate_args(email=None, age=None, mobile=None, gender=None, blood_group=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if email:
                validate_email(email)
            if age:
                validate_age(age)
            if mobile:
                validate_mobile(mobile)
            if gender:
                validate_gender(gender)
            if blood_group:
                validate_blood_group(blood_group)
            return func(*args, **kwargs)
        return wrapper
    return decorator
