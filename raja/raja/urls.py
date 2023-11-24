from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofasquareprism/',views.primsarea,name="areaofasquareprism"),
    path('',views.primsarea,name="areaofasquareprismisroot")
]