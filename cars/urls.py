from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.carDetail, name='carDetail'),
    path('search', views.search, name='search'),
]
