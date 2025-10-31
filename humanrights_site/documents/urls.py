from django.urls import path
from documents import views


app_name = 'documents'
urlpatterns = [
    path('', views.AllAttachmentsListView.as_view(), name='all-attachments'),
]
