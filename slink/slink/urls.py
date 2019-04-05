from django.contrib import admin
from django import urls

from api import views


urlpatterns = [
    urls.path('admin/', admin.site.urls),
    urls.path('', views.get_link, name='get_link'),
    urls.path('links/<link_id>', views.redirect_link, name='redirect_link'),
]
