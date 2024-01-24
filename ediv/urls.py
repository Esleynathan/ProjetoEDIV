from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authenticacao.urls')),
    path('services/', include('services.urls')),
    path('manager/', include('manager.urls')),
]
