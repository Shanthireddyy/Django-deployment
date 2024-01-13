import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'revisonpro.settings')

import django
django.setup()

from apprevision.models import User
from faker import Faker


fake_obj=Faker()

def populate(N=8):
    for i in range(N):
        fake_name=fake_obj.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_email=fake_obj.email()


        user=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]
if __name__=='__main__':
    print("POPULATING DATABASES")
    populate(12)
    print("COMPLETE")




