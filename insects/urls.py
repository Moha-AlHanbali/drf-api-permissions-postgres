from django.urls import path
from .views import InsectListView, InsectDetailView

urlpatterns = [
    path('', InsectListView.as_view(), name = 'insect_list'),
    path('<int:pk>', InsectDetailView.as_view(), name = 'insect_detail'),
]