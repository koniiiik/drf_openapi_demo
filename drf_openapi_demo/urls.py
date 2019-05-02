from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework.renderers import BrowsableAPIRenderer, JSONOpenAPIRenderer, OpenAPIRenderer
from rest_framework.schemas import get_schema_view

from . import api


router = routers.DefaultRouter()
router.register('students', api.StudentViewSet)
router.register('universities', api.UniversityViewSet)


schema_urlpatterns = [
    url(r'^api/', include(router.urls)),
]

schema_view = get_schema_view(
    title="Student & Uni API",
    patterns=schema_urlpatterns,
    renderer_classes=[BrowsableAPIRenderer, OpenAPIRenderer, JSONOpenAPIRenderer],
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + schema_urlpatterns + [
    url(r'^api/schema$', schema_view),
    url(r'^api/schema.json$', schema_view, {'format': 'openapi-json'}),
    url(r'^api/schema.y(?:a?)ml$', schema_view, {'format': 'openapi'}),
]
