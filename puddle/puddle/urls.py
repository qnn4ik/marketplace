from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.urls import path, include
from core.views import *
from item.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # get rid of the last line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
