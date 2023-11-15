from django.urls import path
from taverne.views import taverne_view,client_detail,activite_detail

urlpatterns = [
    path('', taverne_view, name='taverne_view'),
    path('client/<str:pk>/', client_detail, name='client_detail'),
    path('activite/<str:pk>/', activite_detail, name='activite_detail'),
    path('client/<str:pk>/?<str:msg>', client_detail, name='client_detail_mes'),
]
