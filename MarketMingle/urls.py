from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    # path('items/', include('item.urls')),
    #               path('dashboard/', include('dashboard.urls')),
    #               path('inbox/', include('conversation.urls')),

]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # assert isinstance(settings.MEDIA_ROOT, object)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
