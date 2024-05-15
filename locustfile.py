
from locust import HttpUser, task, between
import random
import string

def random_string(length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_email():
    """Generate a random email address"""
    return f"{random_string(10)}@example.com"

class WebsiteUser(HttpUser):
    """
    To run call in bash:           locust 
    To run on 4 cores:             locust --processes 4
    To run on all available cores: locust --processes -1
    """
    
    wait_time = between(0.5, 1)

    @task
    def register(self):
        # Generate random data for each user
        user_data = {
            "email": random_email(),
            "username": random_string(8),
            "first_name": random_string(6),
            "last_name": random_string(7),
            "gender": random.choice(["m", "f", "o"]),
            "country": random.choice(["US", "CA", "UK", "AU", "NZ"]),
            "isActive": random.choice([True, False]),
            "password": random_string(12)
        }

        # Send a POST request with the generated user data
        self.client.post("/users/", json=user_data)
