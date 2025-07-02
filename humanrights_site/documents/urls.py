from django.urls import path
from .views import AllAttachmentsListView

urlpatterns = [
    path('', AllAttachmentsListView.as_view(), name='all_attachments'),
]
