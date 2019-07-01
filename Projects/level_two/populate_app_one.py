import os
import django
# configure settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'level_two.settings')

# set up Django
django.setup()

# Create a fake population script
import random
from app_one.models import User
from faker import Faker

# Create an instance of the Faker object
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        first = fakegen.first_name()
        last = fakegen.last_name()
        em = fakegen.email()

        # Create a new User entry
        new_user = User.objects.get_or_create(first_name = first, last_name= last, email = em)[0]

if __name__ == "__main__":
    print('Populating Scripts!')
    populate(10)
    print("populating complete!")
