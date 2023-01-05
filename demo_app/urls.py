from django.urls import path
from . import views

urlpatterns = [
    path('', views.racer_list, name='racer_list'),
    path('racer_detail/<int:pk>', views.racer_detail, name='racer_detail')

]