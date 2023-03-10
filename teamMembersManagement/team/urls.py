from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_member/<str:pk>', views.updateMember, name='update_member')
]