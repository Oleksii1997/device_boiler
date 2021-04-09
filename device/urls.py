from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('get_last_data/', views.get_last_data, name="get_last_data"),
    path('admin/', admin.site.urls),
]
