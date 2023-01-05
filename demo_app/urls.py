from django.urls import path
from . import views

urlpatterns = [
    path('', views.racer_list, name='racer_list'),
    path('racer_detail/<int:pk>', views.racer_detail, name='racer_detail'),
    
    path('racer_create_generic', views.RacerCreateView.as_view(), name='racer_create'),
    path('racer_list_generic', views.RacerListView.as_view(), name='racer_list2'),
    path('racer_detail_generic/<int:pk>', views.RacerDetailView.as_view(), name='racer_detail2' ),
    path('racer_update_generic/<int:pk>', views.RacerUpdateView.as_view(), name='racer_update'),
    path('racer_delete_generic/<int:pk>', views.RacerDeleteView.as_view(), name='racer_delete')


]