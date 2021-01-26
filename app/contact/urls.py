from contact.views.contacts import ContactViewSet
from contact.views.excel_files import ExcelFileViewSet
from django.conf.urls import url

urlpatterns = [
    url(r'^excel-files', ExcelFileViewSet.as_view({'post': 'upload_excel_file',
                                                   'get': 'list'})),
    url(r'^contacts', ContactViewSet.as_view({'get': 'list'})),
]
