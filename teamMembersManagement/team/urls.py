from django.urls import path
from .views import MemberList, MemberUpdate, MemberCreate, MemberDelete

urlpatterns = [
    path('', MemberList.as_view(), name='members'),
    path('member-create/', MemberCreate.as_view(), name='member-create'),
    path('member-update/<str:pk>/', MemberUpdate.as_view(), name='member-update'),
    path('member-delete/<str:pk>/', MemberDelete.as_view(), name='member-delete'),
]