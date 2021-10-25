# from django.utils import timezone
import django
from faker import Faker
import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite1.settings')


django.setup()

from userapp.models import User


faker = Faker()


def populate_user(N=5):
    for entry in range(N):
        fake_first_name = faker.first_name_male()
        fake_last_name = faker.last_name_male()
        fake_domain = faker.domain_name()
        fake_email = '{0}.{1}@{2}'.format(fake_first_name.lower(),
                                          fake_last_name.lower(), fake_domain)
        print(fake_email)
        a = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)


if __name__ == '__main__':
    print('Populating user')
    populate_user(10)
    print('Done populating user')
