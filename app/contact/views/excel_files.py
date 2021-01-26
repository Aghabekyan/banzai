from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response

from contact.models import ExcelFile
from contact.serializers.excel_files import ExcelFileSerializer
from helpers.tasks import process_excel_file


class ExcelFileViewSet(viewsets.ViewSet):

    @transaction.atomic
    def upload_excel_file(self, request):
        file = request.FILES.get('file')
        if file:
            instance = ExcelFile.objects.create(file=file)
            transaction.on_commit(lambda: process_excel_file.delay(file_path=instance.file.url))
        else:
            return Response({'message': 'Please select an excel file.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Upload is underway'}, status=status.HTTP_202_ACCEPTED)

    def list(self, request):
        queryset = ExcelFile.objects.all().order_by('-id')
        serializer = ExcelFileSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
