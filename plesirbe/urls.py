from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from plesirbe.view.views import paginated_destination_list, plesir_base_url, list_of_destinations, destination_detail, search_destination

schema_view = get_schema_view(
    openapi.Info(
        title="PlesirBe API",
        default_version='v1',
        description="Dokumentasi API untuk PlesirBe",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("destinations/", list_of_destinations),
    path("", plesir_base_url),
    path("destination/<int:ids>/", destination_detail),
    path("destpaginated/" , paginated_destination_list),
    path('search/', search_destination),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
