from django.conf.urls import include, url
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from account.routers import router
import djoser.urls.authtoken
API_TITLE = 'Criminal Case API'
API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/', include(djoser.urls.authtoken)),
]
