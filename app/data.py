"""
data.py
---------
Contains user data for the project.
"""

class UserData:
    def __init__(self):
        self.records = {
            "kiran": {
                "email": "kiran@example.com",
                "age": 25,
                "mobile": "9876543210",
                "gender": "male",
                "blood_group": "A+",
                "role": "admin"
            },
            "radha": {
                "email": "radha@example.com",
                "age": 30,
                "mobile": "9123456789",
                "gender": "female",
                "blood_group": "B+",
                "role": "user"
            },
            "nkiran": {
                "email": "nkiran@example.com",
                "age": 22,
                "mobile": "9988776655",
                "gender": "female",
                "blood_group": "O+",
                "role": "admin"
            },
            "alice": {
                "email": "alice@example.com",
                "age": 28,
                "mobile": "1234567890",
                "gender": "female",
                "blood_group": "AB+",
                "role": "user"
            }
        }

    def get_user(self, username):
        return self.records.get(username)

    def add_user(self, username, info):
        if username in self.records:
            raise ValueError("User already exists")
        self.records[username] = info

    def remove_user(self, username):
        if username in self.records:
            del self.records[username]
        else:
            raise ValueError("User not found")

user_data = UserData()
