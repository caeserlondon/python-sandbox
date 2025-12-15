import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## Fake Pop Script
import random
from first_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fake_gen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for _ in range(N):
        ####  FOR TOPICS
        # #Add a topic
        # top = add_topic()
        #
        # #Create the fake data
        # fake_url = fake_gen.url()
        # fake_date = fake_gen.date()
        # fake_name = fake_gen.company()
        #
        # # Creat the new page entry
        # webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        #
        # #Creat a fake access record for that webpage
        # acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

        #### FOR USERS
        fake_name = fake_gen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake_gen.email()
        # New User
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("Populating...")
    populate(20)
    print("Done.")
