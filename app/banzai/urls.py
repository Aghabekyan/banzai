from django.conf.urls import url, include

urlpatterns = [
    url(r'api/v1/', include(('contact.urls', 'contacts'), namespace='contacts'))
]
