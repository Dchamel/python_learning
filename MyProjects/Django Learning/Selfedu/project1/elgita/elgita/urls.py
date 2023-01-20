from django.contrib import admin
from django.urls import path, include
from women.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls'))
]

handler404 = pageNotFound
