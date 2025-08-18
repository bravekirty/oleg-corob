from django.urls import path
from .views import AllAttachmentsListView


app_name = 'documents'
urlpatterns = [
    path('', AllAttachmentsListView.as_view(), name='all-attachments'),
]
