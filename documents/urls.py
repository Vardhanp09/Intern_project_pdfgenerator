from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('create/', views.document_create, name='document_create'),
    path('generate-pdf/<int:pk>/', views.generate_pdf, name='generate_pdf'),
]