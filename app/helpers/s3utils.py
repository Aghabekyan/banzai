import os

from storages.backends.s3boto3 import S3Boto3Storage

ENV = os.getenv("ENV")

MediaRootS3BotoStorage = lambda: S3Boto3Storage(location=f'{ENV}/media')
