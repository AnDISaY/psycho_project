from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from cinema import settings

schema_view = get_schema_view(
    openapi.Info(
        title='Psycho Cinema',
        default_version=1,
        description='All anime titles',
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('account/', include('account.urls')),
    path('main/', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
