from rest_framework import serializers

from contact.models import ExcelFile


class ExcelFileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    file_path = serializers.CharField(read_only=True, source="file.url")

    class Meta:
        model = ExcelFile
        fields = ('id', 'file_path')
