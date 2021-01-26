import uuid

from django.db import models
from django.utils import timezone


def upload_to(instance, filename):
    return 'files/%s' % (str(uuid.uuid4()))


class ExcelFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=upload_to, null=False)

    class Meta:
        db_table = "excel_file"


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "contact"
