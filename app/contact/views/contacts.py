from rest_framework import viewsets, status
from rest_framework.response import Response

from contact.models import Contact
from contact.serializers.contacts import ContactSerializer


class ContactViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Contact.objects.all().order_by('-created_at')
        serializer = ContactSerializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
