import datetime

import pandas as pd
from celery import group
from django.db.models import Q
from django.utils import timezone

from banzai import celery_app
from contact.models import Contact


@celery_app.task(bind=True, max_retries=10, acks_late=True)
def store_contact_to_db(self, contact_dict):
    try:
        created_time = timezone.now() - datetime.timedelta(minutes=3)
        contacts_count = Contact.objects.filter(
            Q(email=contact_dict.get('email')) | Q(phone_number=contact_dict.get('phone_number')),
            created_at__gte=created_time
        ).count()

        if not contacts_count:
            Contact.objects.create(**contact_dict)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=10)


@celery_app.task(bind=True, max_retries=10, acks_late=True)
def process_excel_file(self, file_path):
    try:
        data_dict = pd.read_excel(file_path,
                                  header=1,
                                  converters={'Phone Number': str}) \
            .dropna(subset=['Phone Number']).to_dict()

        contact_tasks = []
        for key, val in data_dict['Name'].items():
            contact_dict = {
                'name': val,
                'phone_number': data_dict['Phone Number'][key],
                'email': data_dict['Email Address'][key]
            }
            contact_tasks.append(store_contact_to_db.s(contact_dict=contact_dict))

        group(contact_tasks).delay()
    except Exception as exc:
        raise self.retry(exc=exc, countdown=5)
